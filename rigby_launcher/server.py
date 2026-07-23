import os
import sys
import json
import shutil
import subprocess
import threading
import webbrowser
import urllib.parse
import zipfile
import tempfile
import time
from http.server import HTTPServer, BaseHTTPRequestHandler

HOME = os.path.expanduser("~")
DATA_DIR = os.path.join(HOME, ".local", "share", "rigby-launcher", "data")
SETTINGS_FILE = os.path.join(DATA_DIR, "settings.json")
ITCH_CLIENT_ID = "1ba9b4bfa1ac7759e8420eed4ec863ba"
OAUTH_PORT = 7890

RELEASES = {
    "17.4I": "https://github.com/jogamerforgames2021/AmongUsLauncherNew/releases/download/17.4I/app.zip",
    "17.3I": "https://github.com/jogamerforgames2021/AmongUsLauncherNew/releases/download/17.3I/app.zip",
    "17.2.2I": "https://github.com/jogamerforgames2021/AmongUsLauncherNew/releases/download/17.2.2I/app.zip",
    "17.2.1I": "https://github.com/jogamerforgames2021/AmongUsLauncherNew/releases/download/17.2.1I/app.zip",
    "17.1.0I": "https://github.com/jogamerforgames2021/AmongUsLauncherNew/releases/download/17.1.0I/app.zip",
    "17.0.1I": "https://github.com/jogamerforgames2021/AmongUsLauncherNew/releases/download/17.0.1I/app.zip",
    "17.0.0I": "https://github.com/jogamerforgames2021/AmongUsLauncherNew/releases/download/17.0.0I/app.zip",
    "16.1.0I": "https://github.com/jogamerforgames2021/AmongUsLauncherNew/releases/download/16.1.0I/app.zip",
    "16.0.5I": "https://github.com/jogamerforgames2021/AmongUsLauncherNew/releases/download/16.0.5I/app.zip",
    "16.0.2I": "https://github.com/jogamerforgames2021/AmongUsLauncherNew/releases/download/16.0.2I/app.zip",
}

selected_version = "17.4I"
latest_release_tag = None

SETTINGS_DEFAULTS = {
    "game_dir": "",
    "wine_prefix": os.path.join(HOME, ".wine-au"),
    "wine_binary": "wine",
    "auto_download": True,
    "auto_update": False,
    "auto_launch": False,
    "theme": "dark",
    "launch_delay": 5,
    "fixer_custom_dir": "",
    "installed_version": "",
    "fixer_done": False,
}


def load_settings():
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE) as f:
                return {**SETTINGS_DEFAULTS, **json.load(f)}
        except:
            pass
    return dict(SETTINGS_DEFAULTS)


def save_settings(settings):
    os.makedirs(os.path.dirname(SETTINGS_FILE), exist_ok=True)
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=2)


settings = load_settings()


def detect_game_dir():
    if settings["game_dir"] and os.path.exists(os.path.join(settings["game_dir"], "Among Us.exe")):
        return settings["game_dir"]
    default = os.path.join(HOME, ".wine-au", "drive_c", "Program Files (x86)", "Among Us")
    if os.path.exists(os.path.join(default, "Among Us.exe")):
        settings["game_dir"] = default
        save_settings(settings)
        return default
    return ""


class OAuthServer:
    def __init__(self):
        self.token = None
        self.server = None

    def start(self):
        handler = self._make_handler()
        self.server = HTTPServer(("127.0.0.1", OAUTH_PORT), handler)
        while self.token is None:
            self.server.handle_request()

    def stop(self):
        if self.server:
            self.server.server_close()

    def _make_handler(self):
        oauth = self
        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                if self.path.startswith("/token"):
                    params = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
                    oauth.token = params.get("t", [None])[0]
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(b"""<!DOCTYPE html><html><body style="background:#000;color:#33C759;display:flex;justify-content:center;align-items:center;height:100vh;font-family:-apple-system,BlinkMacSystemFont,sans-serif;margin:0"><div style="text-align:center"><div style="font-size:48px;margin-bottom:12px">&#10004;</div><div style="font-size:20px;font-weight:600">AUTHORIZATION COMPLETE</div><div style="color:#a1a1aa;margin-top:8px;font-size:14px">You can close this tab.</div></div></body></html>""")
                else:
                    self.send_response(200)
                    self.send_header("Content-Type", "text/html")
                    self.end_headers()
                    self.wfile.write(b"""<!DOCTYPE html><html><body style="background:#000;color:#fff;display:flex;justify-content:center;align-items:center;height:100vh;font-family:-apple-system,BlinkMacSystemFont,sans-serif;margin:0;flex-direction:column"><div style="font-size:14px;color:#a1a1aa;margin-bottom:20px">Completing authorization...</div><div style="font-size:13px;color:#6b7280">You may close this tab.</div><script>var h=location.hash;if(h){var t=h.replace(/^#access_token=/,'');if(t) fetch('/token?t='+t);} else { document.body.innerHTML='<div style=text-align:center><div style=font-size:48px;margin-bottom:12px>&#10007;</div><div style=font-size:20px;font-weight:600;color:#ef4444>NO TOKEN RECEIVED</div><div style=color:#a1a1aa;margin-top:8px>Please try again.</div></div>'; }</script></body></html>""")
            def log_message(self, fmt, *args): pass
        return Handler


class APIHandler(BaseHTTPRequestHandler):
    game_download_progress = {"downloading": False, "progress": 0, "extracting": False, "error": ""}
    fixer_status = {"logged_in": False, "username": "", "avatar_url": "", "token": ""}
    fixer_busy = False

    def _send_json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def _send_file(self, path):
        ext = os.path.splitext(path)[1].lower()
        content_types = {
            ".html": "text/html",
            ".css": "text/css",
            ".js": "application/javascript",
            ".png": "image/png",
            ".ico": "image/x-icon",
            ".svg": "image/svg+xml",
            ".json": "application/json",
        }
        ct = content_types.get(ext, "application/octet-stream")
        try:
            with open(path, "rb") as f:
                self.send_response(200)
                self.send_header("Content-Type", ct)
                self.end_headers()
                self.wfile.write(f.read())
        except FileNotFoundError:
            self._send_json({"error": "not found"}, 404)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        from rigby_launcher.html import HTML_INDEX

        if path == "/api/status":
            game_dir = detect_game_dir()
            game_installed = bool(game_dir and os.path.exists(os.path.join(game_dir, "Among Us.exe")))
            wine_ok = sys.platform == "win32" or bool(shutil.which("wine"))
            self._check_existing_fixer_token()
            if latest_release_tag is None:
                threading.Thread(target=self._check_latest_release, daemon=True).start()
            self._send_json({
                "game_installed": game_installed,
                "game_dir": game_dir or "",
                "wine_available": wine_ok,
                "wine_version": self._get_wine_version(),
                "downloading": self.__class__.game_download_progress["downloading"],
                "download_progress": self.__class__.game_download_progress,
                "fixer": self.__class__.fixer_status,
                "fixer_busy": self.__class__.fixer_busy,
                "settings": settings,
                "selected_version": selected_version,
                "installed_version": settings.get("installed_version", ""),
                "latest_release": latest_release_tag,
            })

        elif path == "/api/versions":
            self._send_json({"versions": list(RELEASES.keys()), "selected": selected_version})

        elif path == "/api/fixer/status":
            self._check_existing_fixer_token()
            self._send_json({**self.__class__.fixer_status, "busy": self.__class__.fixer_busy})

        elif path == "/api/fixer/detect-dir":
            detected = self._detect_fixer_dir()
            self._send_json({"dir": detected})

        elif path.startswith("/api/"):
            self._send_json({"error": "unknown endpoint"}, 404)

        else:
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(HTML_INDEX.encode())

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length) if content_length else b"{}"
        try:
            data = json.loads(body) if body else {}
        except:
            data = {}

        if parsed.path == "/api/settings":
            global settings
            for k, v in data.items():
                if k in SETTINGS_DEFAULTS:
                    settings[k] = v
            save_settings(settings)
            self._send_json({"ok": True, "settings": settings})

        elif parsed.path == "/api/browse":
            selected = self._pick_directory()
            self._send_json({"ok": bool(selected), "dir": selected or ""})

        elif parsed.path == "/api/download":
            global selected_version
            version = data.get("version", selected_version)
            if version in RELEASES:
                selected_version = version
            threading.Thread(target=self._download_game, daemon=True).start()
            self._send_json({"ok": True, "message": "Download started"})

        elif parsed.path == "/api/launch":
            self._send_json(self._launch_game())

        elif parsed.path == "/api/fixer/login":
            if self.__class__.fixer_busy:
                self._send_json({"ok": False, "message": "Fixer already running"})
            else:
                self.__class__.fixer_busy = True
                threading.Thread(target=self._run_oauth_fixer, daemon=True).start()
                self._send_json({"ok": True, "message": "OAuth flow started"})

        elif parsed.path == "/api/fixer/set-dir":
            custom_dir = data.get("dir", "")
            if custom_dir:
                settings["fixer_custom_dir"] = custom_dir
                save_settings(settings)
            token = self._save_token_to_dir(custom_dir or settings["fixer_custom_dir"])
            if token:
                self._send_json({"ok": True, "message": "Token saved to custom directory"})
            else:
                self._send_json({"ok": False, "message": "No token available. Login first."}, 400)

        else:
            self._send_json({"error": "unknown endpoint"}, 404)

    def _pick_directory(self):
        pickers = [
            ["zenity", "--file-selection", "--directory", "--title=Select Directory"],
            ["kdialog", "--getexistingdirectory", "--title=Select Directory"],
            ["python3", "-c", "import tkinter as tk; from tkinter import filedialog; root=tk.Tk(); root.withdraw(); print(filedialog.askdirectory())"],
        ]
        for cmd in pickers:
            try:
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
                if result.returncode == 0:
                    path = result.stdout.strip()
                    if path and os.path.isdir(path):
                        return path
            except:
                continue
        return ""

    def _get_wine_version(self):
        try:
            result = subprocess.run(["wine", "--version"], capture_output=True, text=True, timeout=5)
            return result.stdout.strip() or "wine"
        except:
            return ""

    def _detect_fixer_dir(self):
        custom = settings.get("fixer_custom_dir", "")
        if custom and os.path.isdir(custom):
            return custom
        return detect_game_dir()

    def _fixer_target_dir(self):
        if sys.platform == "win32":
            return os.path.join(os.environ.get("USERPROFILE", HOME),
                                "AppData", "LocalLow", "Innersloth", "Among Us")
        wine_prefix = settings.get("wine_prefix", "") or os.path.join(HOME, ".wine-au")
        user = os.environ.get("USER", "user")
        return os.path.join(wine_prefix, "drive_c", "users", user, "AppData", "LocalLow", "Innersloth", "Among Us")

    def _check_existing_fixer_token(self):
        candidates = []
        appdata_itch = os.path.join(self._fixer_target_dir(), "itch")
        if os.path.exists(appdata_itch):
            candidates.append(appdata_itch)
        game_dir = detect_game_dir()
        if game_dir:
            candidates.append(os.path.join(game_dir, "itch"))
        custom_dir = settings.get("fixer_custom_dir", "")
        if custom_dir:
            candidates.append(os.path.join(custom_dir, "itch"))
        for f in candidates:
            if os.path.isfile(f):
                try:
                    with open(f) as fh:
                        token = fh.read().strip()
                    if token:
                        self.__class__.fixer_status["logged_in"] = True
                        self.__class__.fixer_status["token"] = token
                        try:
                            import requests
                            headers = {"Authorization": token}
                            resp = requests.get("https://itch.io/api/1/key/me", headers=headers, timeout=10)
                            if resp.status_code == 200:
                                user = resp.json().get("user", {})
                                self.__class__.fixer_status["username"] = user.get("username", "User")
                                self.__class__.fixer_status["avatar_url"] = user.get("cover_url", "")
                        except:
                            pass
                        return
                except:
                    pass
        self.__class__.fixer_status["logged_in"] = False
        self.__class__.fixer_status["username"] = ""
        self.__class__.fixer_status["avatar_url"] = ""

    def _save_token_to_dir(self, custom_dir):
        if not custom_dir:
            return None
        token = self.__class__.fixer_status.get("token", "")
        if not token:
            return None
        os.makedirs(custom_dir, exist_ok=True)
        target = os.path.join(custom_dir, "itch")
        with open(target, "w") as f:
            f.write(token)
        return token

    def _run_oauth_fixer(self):
        oauth = OAuthServer()
        try:
            auth_url = f"https://itch.io/user/oauth?client_id={ITCH_CLIENT_ID}&scope=profile:me&redirect_uri=http://127.0.0.1:{OAUTH_PORT}&response_type=token"
            webbrowser.open(auth_url)
            oauth.start()
            token = oauth.token
            if token:
                self.__class__.fixer_status["token"] = token
                target_dir = self._fixer_target_dir()
                os.makedirs(target_dir, exist_ok=True)
                with open(os.path.join(target_dir, "itch"), "w") as f:
                    f.write(token)
                self._check_existing_fixer_token()
        finally:
            oauth.stop()
            self.__class__.fixer_busy = False

    def _check_latest_release(self):
        global latest_release_tag
        try:
            import requests
            r = requests.get("https://api.github.com/repos/jogamerforgames2021/AmongUsLauncherNew/releases/latest", timeout=10)
            if r.status_code == 200:
                latest_release_tag = r.json().get("tag_name", "")
        except:
            pass

    def _download_game(self):
        if self.__class__.game_download_progress["downloading"]:
            return
        self.__class__.game_download_progress["downloading"] = True
        self.__class__.game_download_progress["progress"] = 0
        self.__class__.game_download_progress["extracting"] = False
        try:
            import requests
            url = RELEASES.get(selected_version)
            if not url:
                raise RuntimeError(f"No download URL for version {selected_version}")
            install_dir = os.path.join(HOME, ".wine-au", "drive_c", "Program Files (x86)", "Among Us")
            os.makedirs(install_dir, exist_ok=True)
            zip_path = os.path.join(tempfile.gettempdir(), "among-us-app.zip")
            response = requests.get(url, stream=True, timeout=30)
            response.raise_for_status()
            total = int(response.headers.get("content-length", 0))
            downloaded = 0
            with open(zip_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
                    downloaded += len(chunk)
                    if total:
                        self.__class__.game_download_progress["progress"] = int(downloaded / total * 100)
            self.__class__.game_download_progress["extracting"] = True
            with zipfile.ZipFile(zip_path, "r") as zf:
                total_files = len(zf.namelist())
                for i, name in enumerate(zf.namelist()):
                    zf.extract(name, install_dir)
                    self.__class__.game_download_progress["progress"] = int((i + 1) / total_files * 100)
            os.unlink(zip_path)
            game_dir = install_dir
            if not os.path.exists(os.path.join(game_dir, "Among Us.exe")):
                for root, dirs, files in os.walk(install_dir):
                    if "Among Us.exe" in files:
                        game_dir = root
                        break
            settings["game_dir"] = game_dir
            settings["installed_version"] = selected_version
            save_settings(settings)
        except Exception as e:
            self.__class__.game_download_progress["error"] = str(e)
        finally:
            self.__class__.game_download_progress["downloading"] = False
            self.__class__.game_download_progress["extracting"] = False

    def _launch_game(self):
        game_dir = detect_game_dir()
        if not game_dir:
            return {"ok": False, "message": "Game not installed. Download it first."}
        exe_path = os.path.join(game_dir, "Among Us.exe")
        if not os.path.exists(exe_path):
            return {"ok": False, "message": "Among Us.exe not found in game directory."}

        if sys.platform == "win32":
            try:
                subprocess.Popen([exe_path], cwd=game_dir)
                return {"ok": True, "message": "Game launched!"}
            except Exception as e:
                return {"ok": False, "message": str(e)}

        wine_bin = settings.get("wine_binary", "") or "wine"
        wine_prefix = settings.get("wine_prefix", "") or os.path.join(HOME, ".wine-au")
        env = {"WINEPREFIX": wine_prefix, "HOME": HOME,
               "USER": os.environ.get("USER", ""),
               "DISPLAY": os.environ.get("DISPLAY", ":0"),
               "XAUTHORITY": os.environ.get("XAUTHORITY", os.path.join(HOME, ".Xauthority")),
               "WAYLAND_DISPLAY": os.environ.get("WAYLAND_DISPLAY", ""),
               "PATH": "/usr/local/bin:/usr/bin:/bin",
               "DXVK_ASYNC": "1"}

        try:
            subprocess.Popen([wine_bin, exe_path], cwd=game_dir, env=env)
            return {"ok": True, "message": "Game launched!"}
        except FileNotFoundError:
            return {"ok": False, "message": f"Wine not found at '{wine_bin}'. Install wine."}
        except Exception as e:
            return {"ok": False, "message": str(e)}


LOG_FILE = os.path.join(DATA_DIR, "server.log")

def log(msg):
    try:
        os.makedirs(DATA_DIR, exist_ok=True)
        with open(LOG_FILE, "a") as f:
            f.write(f"[{time.strftime('%H:%M:%S')}] {msg}\n")
    except:
        pass

os.makedirs(DATA_DIR, exist_ok=True)
