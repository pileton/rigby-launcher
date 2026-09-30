import os
import signal
import sys
import json
import shutil
import subprocess
import threading
import webbrowser
import urllib.parse
import zipfile
import tempfile
import hashlib
import time
from http.server import HTTPServer, BaseHTTPRequestHandler

HOME = os.path.expanduser("~")
DATA_DIR = os.path.join(HOME, ".local", "share", "rigby-launcher", "data")
SETTINGS_FILE = os.path.join(DATA_DIR, "settings.json")
ITCH_CLIENT_ID = "1ba9b4bfa1ac7759e8420eed4ec863ba"
OAUTH_PORT = 7890

LAUNCHER_REPO = "pileton/rigby-launcher"
LAUNCHER_VERSION = "0.6"

RELEASES = {
    "19I": "https://github.com/jogamerforgames2021/AmongUsLauncherNew/releases/download/19I/app.zip",
    "18I": "https://github.com/jogamerforgames2021/AmongUsLauncherNew/releases/download/18I/app.zip",
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

selected_version = "18I"
latest_release_tag = None

LAUNCHER_REPO = "pileton/rigby-launcher"
LAUNCHER_VERSION = "0.6"
BEPINEX_REPO = "BepInEx/BepInEx"
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.6 (KHTML, like Gecko) Chrome/120.0 Safari/537.6"

_HTTP_SESSION = None

def _http_session():
    global _HTTP_SESSION
    if _HTTP_SESSION is None:
        import requests
        from requests.adapters import HTTPAdapter
        sess = requests.Session()
        sess.headers["User-Agent"] = USER_AGENT
        try:
            from urllib3.util import Retry
            retry = Retry(total=3, backoff_factor=0.8, allowed_methods=frozenset(["GET", "HEAD"]),
                          status_forcelist=[429, 500, 502, 503, 504])
            adapter = HTTPAdapter(max_retries=retry)
            sess.mount("http://", adapter)
            sess.mount("https://", adapter)
        except Exception:
            pass
        _HTTP_SESSION = sess
    return _HTTP_SESSION

def _http_get(url, **kwargs):
    """requests.get on the shared retrying session (small JSON calls)."""
    return _http_session().get(url, **kwargs)

def _download(url, dest_path):
    """Download url -> dest_path robustly.

    Tries the retrying requests session first. If the connection times out or is
    refused (python-requests intermittently cannot reach github.com while curl
    can), fall back to curl with its own retries. Returns (ok, message).
    """
    try:
        resp = _http_get(url, stream=True, timeout=(15, 180))
        resp.raise_for_status()
        with open(dest_path, "wb") as f:
            for chunk in resp.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        return True, ""
    except Exception as e:
        last = str(e) or type(e).__name__
    try:
        import shutil, subprocess
        curl = shutil.which("curl")
        if curl:
            proc = subprocess.run(
                [curl, "-L", "--fail", "--retry", "4", "--retry-delay", "2",
                 "--max-time", "300", "-A", USER_AGENT, "-o", dest_path, url],
                timeout=320, capture_output=True)
            if proc.returncode == 0 and os.path.exists(dest_path) and os.path.getsize(dest_path) > 0:
                return True, ""
            last = last or (proc.stderr.decode(errors="replace")[:200] if proc.stderr else "")
    except Exception as e:
        last = last or str(e)
    return False, ("Could not download the file (check your network and that the "
                 "URL is reachable): " + last[:300])
    
MODS = [
    {
        "id": "hydra",
        "name": "Hydra",
        "version": "18I",
        "categories": ["Menu"],
        "description": "Hydra mod menu for Among Us with a wide range of gameplay features.",
        "image": "https://files.catbox.moe/ajyi00.png",
        "url": "https://github.com/MrDiamond64/Hydra/releases/download/v2.0.0/HydraMenu.dll",
        
        "bepinex": {
            "version": "6.0.0-be.785",
            "win_x86": "https://github.com/MrDiamond64/Hydra/releases/download/v2.0.0/BepInEx-Unity.IL2CPP-win-x86-6.0.0-be.785+6abdba4.zip",
            "win_x64": "https://github.com/MrDiamond64/Hydra/releases/download/v2.0.0/BepInEx-Unity.IL2CPP-win-x64-6.0.0-be.785+6abdba4.zip",
        },
    },
    {
        "id": "malum",
        "name": "Malum",
        "version": "18I",
        "categories": ["Menu"],
        "description": "Malum mod menu for Among Us (latest release).",
        "image": "https://files.catbox.moe/sg12ea.png",
        "url": "https://github.com/scp222thj/MalumMenu/releases/download/v3.3.0/MalumMenu-3.3.0.dll",
    },
    {
        "id": "aunlocker",
        "name": "AUnlocker",
        "version": ["18I", "17.4I"],
        "categories": ["Cosmetics"],
        "description": "AUnlocker - unlocks all hats, pets, skins and visors locally. Compatible with game versions 18I and 17.4I.",
        "image": "https://files.catbox.moe/dqmtno.png",
        "url": "https://github.com/astra1dev/AUnlocker/releases/download/v1.3.1/AUnlocker_v1.3.1.dll",
    },
]

ICON_CACHE_DIR = os.path.join(HOME, ".cache", "rigby-launcher", "icons")


def _icon_hash(url):
    return hashlib.sha1(url.encode("utf-8")).hexdigest()[:16]


ICON_URLS = {}
for _m in MODS:
    _h = _icon_hash(_m["image"])
    ICON_URLS[_h] = _m["image"]
    _m["image"] = "/api/icon/" + _h


def _prefetch_icons():
    """Warm the icon cache in a background thread so the first Mods open is instant."""
    try:
        os.makedirs(ICON_CACHE_DIR, exist_ok=True)
        for h, src in list(ICON_URLS.items()):
            cpath = os.path.join(ICON_CACHE_DIR, h + ".png")
            if os.path.exists(cpath):
                continue
            try:
                _download(src, cpath)
            except Exception:
                pass
    except Exception:
        pass

SETTINGS_DEFAULTS = {
    "game_dir": "",
    "wine_prefix": os.path.join(HOME, ".wine-au"),
    "wine_binary": "wine",
    "auto_download": True,
    "auto_update": False,
    "auto_launch": False,
    "beta_watchdog": False,
    "beta_terminate": False,
    "beta_limit_launcher": False,
    "theme": "dark",
    "launch_delay": 5,
    "fixer_custom_dir": "",
    "installed_version": "",
    "fixer_done": False,
    "accounts": [],
    "installed_mods": [],
    "selected_version": "18I",
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

selected_version = settings.get("selected_version") or selected_version

def _au_game_procs():
    """Return [(pid, cpu_pct, rss_bytes, args)] for running Among Us processes."""
    if os.name == "nt":
        return []
    try:
        out = subprocess.run(["ps", "-eo", "pid=,pcpu=,rss=,args="],
                             capture_output=True, text=True, timeout=5).stdout
    except Exception:
        return []
    res = []
    self_pid = os.getpid()
    for line in out.splitlines():
        parts = line.split(None, 3)
        if len(parts) < 4:
            continue
        pid, pcpu, rss, args = parts
        low = args.lower()
        if pid == str(self_pid):
            continue
        if "rigby" in low or "amongus-launcher" in low:
            continue
        if "among us" in low or "amongus.exe" in low or "amogus" in low:
            try:
                res.append((int(pid), float(pcpu), int(rss) * 1024, args))
            except ValueError:
                pass
    return res

_last_launch_ts = 0.0

_beta_mon_started = False
def start_beta_monitor():
    global _beta_mon_started
    if _beta_mon_started:
        return
    _beta_mon_started = True
    self_pid = os.getpid()
    def loop():
        high_streak = 0
        while True:
            time.sleep(5)
            try:
                if not settings.get("beta_watchdog"):
                    high_streak = 0
                    continue
                procs = _au_game_procs()
                if not procs:
                    high_streak = 0
                    continue
                cpu = max(p[1] for p in procs)
                if cpu > 90.0:
                    high_streak = min(high_streak + 1, 99)
                elif high_streak > 0:
                    high_streak -= 1
                if high_streak >= 3 and settings.get("beta_terminate"):
                    killed = 0
                    for pid, _, _, _ in procs:
                        if pid == self_pid:
                            continue
                        try:
                            os.kill(pid, signal.SIGKILL)
                            killed += 1
                        except Exception:
                            pass
                    print("[beta-watchdog] terminated Among Us (cpu %.0f%%, sustained %ds)"
                          % (cpu, high_streak * 5), flush=True)
                    high_streak = 0
                elif high_streak >= 2 and settings.get("beta_limit_launcher"):
                    try:
                        os.nice(10)
                    except Exception:
                        pass
            except Exception:
                pass
    threading.Thread(target=loop, daemon=True).start()

start_beta_monitor()


def _default_folder():
    return os.path.join(HOME, ".wine-au", "drive_c", "Program Files (x86)", "Among Us")


def _version_folder(version):
    return os.path.join(HOME, ".wine-au", "drive_c", "Program Files (x86)", "Among Us_" + version)


def _is_version_installed(version):
    if os.path.exists(os.path.join(_version_folder(version), "Among Us.exe")):
        return True
    if version == settings.get("primary_version", ""):
        if os.path.exists(os.path.join(_default_folder(), "Among Us.exe")):
            return True
    return False


def _folder_for_version(version):
    vf = _version_folder(version)
    if os.path.exists(os.path.join(vf, "Among Us.exe")):
        return vf
    if version == settings.get("primary_version", "") and os.path.exists(os.path.join(_default_folder(), "Among Us.exe")):
        return _default_folder()
    return ""


def detect_game_dir():
    f = _folder_for_version(selected_version)
    if f:
        return f
    if settings["game_dir"] and os.path.exists(os.path.join(settings["game_dir"], "Among Us.exe")):
        return settings["game_dir"]
    default = _default_folder()
    if os.path.exists(os.path.join(default, "Among Us.exe")):
        if not settings.get("primary_version"):
            settings["primary_version"] = settings.get("installed_version", selected_version)
            save_settings(settings)
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
    game_download_progress = {"downloading": False, "progress": 0, "extracting": False, "error": "", "speed": 0, "bytes": 0, "total": 0}
    fixer_status = {"logged_in": False, "username": "", "avatar_url": "", "token": ""}
    fixer_busy = False

    def _send_json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Cache-Control", "no-store")
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
                "installed_version": (selected_version if _is_version_installed(selected_version) else settings.get("installed_version", "")),
                "installed_versions": [v for v in RELEASES if _is_version_installed(v)],
                "latest_release": latest_release_tag,
                "versions": list(RELEASES.keys()),
            })

        elif path == "/api/versions":
            self._send_json({"versions": list(RELEASES.keys()), "selected": selected_version})

        elif path == "/api/fixer/status":
            self._check_existing_fixer_token()
            self._send_json({**self.__class__.fixer_status, "busy": self.__class__.fixer_busy})

        elif path == "/api/accounts":
            accounts = settings.get("accounts", [])
            active_token = ""
            itch_file = os.path.join(self._fixer_target_dir(), "itch")
            if os.path.exists(itch_file):
                try:
                    with open(itch_file) as f:
                        active_token = f.read().strip()
                except:
                    pass
            for acc in accounts:
                acc["active"] = acc.get("token", "") == active_token
            self._send_json({"accounts": accounts, "max": 5})

        elif path == "/api/fixer/detect-dir":
            detected = self._detect_fixer_dir()
            self._send_json({"dir": detected})

        elif path == "/api/launcher/latest":
            self._send_json(self._launcher_latest())

        elif path == "/api/mods":
            bdir, game_dir = self._bepinex_dir()
            versions = list(RELEASES.keys())
            categories = sorted(set(c for m in MODS for c in m["categories"]))
            self._send_json({
                "versions": versions,
                "categories": categories,
                "mods": MODS,
                "installed": self._installed_mods(),
                "bepinex_installed": bool(game_dir and os.path.isdir(bdir)),
                "current_version": selected_version,
            })

        elif path.startswith("/api/icon/"):
            h = path.rsplit("/", 1)[-1]
            src = ICON_URLS.get(h)
            if not src:
                self._send_json({"error": "unknown icon"}, 404)
            else:
                os.makedirs(ICON_CACHE_DIR, exist_ok=True)
                cpath = os.path.join(ICON_CACHE_DIR, h + ".png")
                if not os.path.exists(cpath):
                    ok, _msg = _download(src, cpath)
                    if not ok or not os.path.exists(cpath):
                        self.send_response(302)
                        self.send_header("Location", src)
                        self.end_headers()
                        return
                try:
                    self.send_response(200)
                    self.send_header("Content-Type", "image/png")
                    self.send_header("Cache-Control", "public, max-age=31536000")
                    self.end_headers()
                    with open(cpath, "rb") as f:
                        self.wfile.write(f.read())
                except Exception:
                    self._send_json({"error": "icon error"}, 500)

        elif path.startswith("/api/"):
            self._send_json({"error": "unknown endpoint"}, 404)

        else:
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
            self.send_header("Pragma", "no-cache")
            self.send_header("Expires", "0")
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

        global selected_version

        if parsed.path == "/api/settings":
            global settings
            for k, v in data.items():
                if k in SETTINGS_DEFAULTS:
                    settings[k] = v
            save_settings(settings)
            self._send_json({"ok": True, "settings": settings})

        elif parsed.path == "/api/versions":
            version = data.get("version", selected_version)
            if version in RELEASES:
                selected_version = version
                settings["selected_version"] = version
                save_settings(settings)
            self._send_json({"ok": True, "selected": selected_version})

        elif parsed.path == "/api/browse":
            selected = self._pick_directory()
            self._send_json({"ok": bool(selected), "dir": selected or ""})

        elif parsed.path == "/api/download":
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

        elif parsed.path == "/api/accounts/add":
            if self.__class__.fixer_busy:
                self._send_json({"ok": False, "message": "Login already in progress"})
                return
            accounts = settings.get("accounts", [])
            if len(accounts) >= 5:
                self._send_json({"ok": False, "message": "Maximum 5 accounts reached"})
                return
            self.__class__.fixer_busy = True
            threading.Thread(target=self._run_account_add, daemon=True).start()
            self._send_json({"ok": True, "message": "OAuth flow started"})

        elif parsed.path == "/api/accounts/switch":
            token = data.get("token", "")
            if not token:
                self._send_json({"ok": False, "message": "No token provided"}, 400)
                return
            target_dir = self._fixer_target_dir()
            os.makedirs(target_dir, exist_ok=True)
            with open(os.path.join(target_dir, "itch"), "w") as f:
                f.write(token)
            self._check_existing_fixer_token()
            self._send_json({"ok": True, "message": "Switched account"})

        elif parsed.path == "/api/accounts/remove":
            token = data.get("token", "")
            accounts = [a for a in settings.get("accounts", []) if a.get("token", "") != token]
            settings["accounts"] = accounts
            save_settings(settings)
            self._send_json({"ok": True, "accounts": accounts})

        elif parsed.path == "/api/launcher/update":
            self._send_json(self._launcher_install())

        elif parsed.path.startswith("/api/mods/install"):
            mod_id = parsed.path.rsplit("/", 1)[-1]
            self._send_json(self._install_mod(mod_id))

        elif parsed.path.startswith("/api/mods/remove"):
            mod_id = parsed.path.rsplit("/", 1)[-1]
            self._send_json(self._remove_mod(mod_id))

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
                                self.__class__.fixer_status["username"] = user.get("username") or user.get("display_name") or "User"
                                self.__class__.fixer_status["avatar_url"] = user.get("cover_url") or user.get("avatar_url") or ""
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
                username = self.__class__.fixer_status.get("username", "User")
                avatar_url = self.__class__.fixer_status.get("avatar_url", "")
                accounts = list(settings.get("accounts", []))
                idx = next((i for i, a in enumerate(accounts) if a.get("token", "") == token), None)
                if idx is None:
                    idx = next((i for i, a in enumerate(accounts) if a.get("username", "") == username), None)
                if idx is not None:
                    accounts[idx]["token"] = token
                    accounts[idx]["avatar_url"] = avatar_url
                    accounts[idx]["username"] = username
                else:
                    accounts.append({"token": token, "username": username, "avatar_url": avatar_url})
                settings["accounts"] = accounts
                save_settings(settings)
        finally:
            oauth.stop()
            self.__class__.fixer_busy = False

    def _run_account_add(self):
        oauth = OAuthServer()
        try:
            auth_url = f"https://itch.io/user/oauth?client_id={ITCH_CLIENT_ID}&scope=profile:me&redirect_uri=http://127.0.0.1:{OAUTH_PORT}&response_type=token"
            webbrowser.open(auth_url)
            oauth.start()
            token = oauth.token
            if not token:
                return
            username = "User"
            avatar_url = ""
            try:
                import requests
                r = requests.get("https://itch.io/api/1/key/me", headers={"Authorization": token}, timeout=10)
                if r.status_code == 200:
                    u = r.json().get("user", {})
                    username = u.get("username", "User")
                    avatar_url = u.get("cover_url", "")
            except:
                pass
            accounts = list(settings.get("accounts", []))
            accounts.append({"token": token, "username": username, "avatar_url": avatar_url})
            settings["accounts"] = accounts
            save_settings(settings)
            target_dir = self._fixer_target_dir()
            os.makedirs(target_dir, exist_ok=True)
            with open(os.path.join(target_dir, "itch"), "w") as f:
                f.write(token)
            self.__class__.fixer_status["token"] = token
            self.__class__.fixer_status["username"] = username
            self.__class__.fixer_status["avatar_url"] = avatar_url
            self.__class__.fixer_status["logged_in"] = True
        finally:
            oauth.stop()
            self.__class__.fixer_busy = False

    def _check_latest_release(self):
        global latest_release_tag
        if latest_release_tag is not None:
            return
        try:
            import requests
            r = requests.get("https://api.github.com/repos/jogamerforgames2021/AmongUsLauncherNew/releases/latest",
                             timeout=10, headers={"User-Agent": USER_AGENT})
            if r.status_code == 200:
                latest_release_tag = r.json().get("tag_name", "")
            else:
                latest_release_tag = ""
        except Exception:
            latest_release_tag = ""

    def _pkg_type(self):
        if sys.platform == "win32":
            return "exe"
        if shutil.which("dpkg-deb"):
            return "deb"
        return "arch"

    def _version_key(self, v):
        key = []
        for part in str(v).lstrip("v").split("."):
            num = ""
            for ch in part:
                if ch.isdigit():
                    num += ch
                else:
                    break
            key.append(int(num) if num else 0)
        return tuple(key)

    def _launcher_latest(self):
        pkg = self._pkg_type()
        result = {"available": False, "pkg_type": pkg, "current_version": LAUNCHER_VERSION,
                  "latest_version": None, "asset_name": None, "download_url": None}
        try:
            import requests
            r = requests.get(f"https://api.github.com/repos/{LAUNCHER_REPO}/releases/latest", timeout=10, headers={"User-Agent": USER_AGENT})
            if r.status_code != 200:
                return result
            rel = r.json()
            tag = rel.get("tag_name", "")
            latest = tag.split("_", 1)[-1] if "_" in tag else tag
            suffix_map = {"deb": ".deb", "arch": ".pkg.tar.zst", "exe": ".exe"}
            suffix = suffix_map.get(pkg, "")
            asset = None
            if suffix:
                asset = next((a for a in rel.get("assets", []) if a["name"].endswith(suffix)), None)
            result["latest_version"] = latest
            if asset:
                result["asset_name"] = asset["name"]
                result["download_url"] = asset["browser_download_url"]
                if self._version_key(latest) > self._version_key(LAUNCHER_VERSION):
                    result["available"] = True
        except Exception:
            pass
        return result

    def _copy_tree(self, src, dst):
        for root, dirs, files in os.walk(src):
            rel = os.path.relpath(root, src)
            target = dst if rel == "." else os.path.join(dst, rel)
            os.makedirs(target, exist_ok=True)
            for f in files:
                shutil.copy2(os.path.join(root, f), os.path.join(target, f))

    def _launcher_install(self):
        info = self._launcher_latest()
        if not info.get("download_url"):
            return {"ok": False, "message": "No launcher update available or no package for your system."}
        import requests
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix="_" + (info.get("asset_name") or ".bin"))
        staging = tempfile.mkdtemp(prefix="rigby-update-")
        try:
            ok, msg = _download(info["download_url"], tmp.name)
            if not ok:
                return {"ok": False, "message": "Launcher download failed: " + (msg or "network error. Check your connection and the GitHub release.")}
            tmp.close()
            if info["pkg_type"] == "arch":
                rc = subprocess.run(["tar", "-xf", tmp.name, "-C", staging], capture_output=True, text=True, timeout=180)
            elif info["pkg_type"] == "deb":
                if not shutil.which("dpkg-deb"):
                    return {"ok": False, "message": "dpkg-deb is not installed; cannot extract the .deb. Install dpkg-deb or run: sudo dpkg -i <file>.deb"}
                rc = subprocess.run(["dpkg-deb", "-x", tmp.name, staging], capture_output=True, text=True, timeout=180)
            else:
                return {"ok": True, "message": "Download the Windows .exe from the GitHub releases and install it manually."}
            if rc.returncode != 0:
                return {"ok": False, "message": "Extraction failed: " + (rc.stderr or rc.stdout or "unknown error").strip()[:300]}
            src_usr = os.path.join(staging, "usr")
            if not os.path.isdir(src_usr):
                return {"ok": False, "message": "Extracted archive has no /usr tree."}
            if os.access("/usr", os.W_OK):
                self._copy_tree(src_usr, "/usr")
                binp = os.path.join("/usr", "bin", "rigby-launcher")
                if os.path.exists(binp):
                    os.chmod(binp, 0o755)
                return {"ok": True, "message": f"Launcher updated to {info.get('latest_version')}. Restart the launcher to use it.", "version": info.get("latest_version")}
            # Non-root: portable install into ~/.local (no dpkg -i, works on Mint/Debian without sudo)
            local = os.path.join(HOME, ".local")
            self._copy_tree(src_usr, local)
            binp = os.path.join(local, "bin", "rigby-launcher")
            os.makedirs(os.path.dirname(binp), exist_ok=True)
            share = os.path.join(local, "share", "rigby-launcher")
            with open(binp, "w") as bf:
                bf.write("#!/bin/sh\nexec env PYTHONPATH=\"" + share + "\" python3 -m rigby_launcher \"$@\"\n")
            os.chmod(binp, 0o755)
            return {"ok": True, "message": f"Updated to {info.get('latest_version')} into ~/.local. Restart the launcher with ~/.local/bin/rigby-launcher.", "version": info.get("latest_version")}
        except Exception as e:
            return {"ok": False, "message": f"Update failed: {e}"}
        finally:
            try:
                os.unlink(tmp.name)
            except Exception:
                pass
            shutil.rmtree(staging, ignore_errors=True)

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
            install_dir = _version_folder(selected_version)
            os.makedirs(install_dir, exist_ok=True)
            zip_path = os.path.join(tempfile.gettempdir(), "among-us-app.zip")
            response = _http_get(url, stream=True, timeout=(15, 180))
            response.raise_for_status()
            total = int(response.headers.get("content-length", 0))
            downloaded = 0
            last_bytes = 0
            last_t = time.time()
            self.__class__.game_download_progress["total"] = total
            self.__class__.game_download_progress["bytes"] = 0
            self.__class__.game_download_progress["speed"] = 0
            with open(zip_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
                    downloaded += len(chunk)
                    now = time.time()
                    if now - last_t >= 0.25:
                        self.__class__.game_download_progress["speed"] = int((downloaded - last_bytes) / (now - last_t))
                        last_bytes = downloaded
                        last_t = now
                    if total:
                        self.__class__.game_download_progress["progress"] = int(downloaded / total * 100)
                    self.__class__.game_download_progress["bytes"] = downloaded
            self.__class__.game_download_progress["speed"] = 0
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
            iv = settings.get("installed_versions", [])
            if selected_version not in iv:
                iv.append(selected_version)
            settings["installed_versions"] = iv
            save_settings(settings)
        except Exception as e:
            self.__class__.game_download_progress["error"] = str(e)
        finally:
            self.__class__.game_download_progress["downloading"] = False
            self.__class__.game_download_progress["extracting"] = False

    def _bepinex_dir(self):
        game_dir = detect_game_dir() or ""
        if not game_dir:
            return None, ""
        return os.path.join(game_dir, "BepInEx"), game_dir

    def _installed_mods(self):
        return list(settings.get("installed_mods", []))

    def _exe_arch(self, game_dir):
        """Return 'x86' or 'x64' from Among Us.exe's PE optional-header magic."""
        arch = "x86"
        exe_path = os.path.join(game_dir, "Among Us.exe")
        try:
            with open(exe_path, "rb") as ef:
                if ef.read(2) == b"MZ":
                    ef.seek(0x3C)
                    pe = int.from_bytes(ef.read(4), "little")
                    ef.seek(pe)
                    if ef.read(4) == b"PE\x00\x00":
                        ef.seek(pe + 24)
                        magic = int.from_bytes(ef.read(2), "little")
                        arch = "x64" if magic == 0x20B else "x86"
        except Exception:
            pass
        return arch

    def _install_bepinex(self, bepinex_url=None, version=None):
        bdir, game_dir = self._bepinex_dir()
        if not game_dir:
            return {"ok": False, "message": "Game directory not found. Install the game first."}
        if os.path.isdir(bdir):
            shutil.rmtree(bdir, ignore_errors=True)
        for f in ("winhttp.dll", "doorstop_config.ini", ".doorstop_version"):
            p = os.path.join(game_dir, f)
            if os.path.exists(p):
                try:
                    os.remove(p)
                except OSError:
                    pass
        dotnet_dir = os.path.join(game_dir, "dotnet")
        if os.path.isdir(dotnet_dir):
            shutil.rmtree(dotnet_dir, ignore_errors=True)
        try:
            import requests
            if bepinex_url:
                zip_path = os.path.join(tempfile.gettempdir(), "bepinex.zip")
                ok, msg = _download(bepinex_url, zip_path)
                if not ok:
                    return {"ok": False, "message": "BepInEx download failed: " + (msg or "network error. Check your connection.")}
                with zipfile.ZipFile(zip_path, "r") as zf:
                    zf.extractall(game_dir)
                os.unlink(zip_path)
                if version:
                    try:
                        os.makedirs(bdir, exist_ok=True)
                        with open(os.path.join(bdir, ".rigby_bepinex_version"), "w") as vf:
                            vf.write(version)
                    except Exception:
                        pass
                return {"ok": True, "message": "BepInEx installed"}
            r = _http_get(f"https://api.github.com/repos/{BEPINEX_REPO}/releases?per_page=40", timeout=(10, 60))
            if r.status_code != 200:
                return {"ok": False, "message": "Could not reach BepInEx releases."}
            rels = r.json()
            rel = next((x for x in rels if x.get("tag_name", "").startswith("v6.")), None)
            if not rel:
                rel = next((x for x in rels if not x.get("prerelease", False)), None)
            all_assets = rel.get("assets", []) if rel else []
            arch = "x86"
            exe_path = os.path.join(game_dir, "Among Us.exe")
            try:
                with open(exe_path, "rb") as ef:
                    if ef.read(2) == b"MZ":
                        ef.seek(0x3C)
                        pe = int.from_bytes(ef.read(4), "little")
                        ef.seek(pe)
                        if ef.read(4) == b"PE\x00\x00":
                            ef.seek(pe + 24)
                            magic = int.from_bytes(ef.read(2), "little")
                            arch = "x64" if magic == 0x20B else "x86"
            except Exception:
                pass
            target = "Unity.IL2CPP-win-" + arch
            asset = next((a for a in all_assets if target in a["name"] and a["name"].endswith(".zip")), None)
            if not asset:
                asset = next((a for a in all_assets if "Unity.IL2CPP" in a["name"] and a["name"].endswith(".zip")), None)
            if not asset:
                return {"ok": False, "message": "No BepInEx 6 Il2CPP Windows package for arch %s found." % arch}
            zip_path = os.path.join(tempfile.gettempdir(), "bepinex.zip")
            ok, msg = _download(asset["browser_download_url"], zip_path)
            if not ok:
                return {"ok": False, "message": "BepInEx download failed: " + (msg or "network error. Check your connection.")}
            with zipfile.ZipFile(zip_path, "r") as zf:
                zf.extractall(game_dir)
            os.unlink(zip_path)
            return {"ok": True, "message": "BepInEx installed"}
        except Exception as e:
            return {"ok": False, "message": "BepInEx install failed: " + str(e)}

    def _install_mod(self, mod_id):
        mod = next((m for m in MODS if m["id"] == mod_id), None)
        if not mod:
            return {"ok": False, "message": "Mod not found."}
        url = mod.get("url", "")
        placeholder = ("example.com" in url) or (not url.startswith("http"))
        if placeholder:
            installed = list(settings.get("installed_mods", []))
            if mod["id"] not in [m.get("id") for m in installed]:
                installed.append({"id": mod["id"], "name": mod["name"], "version": mod["version"]})
                settings["installed_mods"] = installed
                save_settings(settings)
            return {"ok": True, "message": "Installed " + mod["name"] + " (placeholder)"}
        bdir, game_dir = self._bepinex_dir()
        if not game_dir:
            return {"ok": False, "message": "Game directory not found. Install the game first."}
        spec = mod.get("bepinex")
        if spec:
            marker = os.path.join(bdir, ".rigby_bepinex_version")
            cur = (open(marker).read().strip() if os.path.isfile(marker) else "")
            need = spec.get("version", "")
            if cur != need:
                arch = self._exe_arch(game_dir)
                url_be = spec.get("win_" + arch)
                if not url_be:
                    return {"ok": False, "message": "No BepInEx build for arch %s" % arch}
                br = self._install_bepinex(url_be, version=need)
                if not br.get("ok"):
                    return br
                bdir, _ = self._bepinex_dir()
        elif not os.path.isdir(bdir):
            br = self._install_bepinex()
            if not br.get("ok"):
                return br
            bdir, _ = self._bepinex_dir()
        try:
            plugins_dir = os.path.join(bdir, "plugins")
            os.makedirs(plugins_dir, exist_ok=True)
            if url.lower().endswith(".dll"):
                dest = os.path.join(plugins_dir, os.path.basename(urllib.parse.urlsplit(url).path))
                ok, msg = _download(url, dest)
                if not ok:
                    if os.path.exists(dest):
                        os.unlink(dest)
                    return {"ok": False, "message": "Download failed for " + mod["name"] + ": " + (msg or "network error. Check your connection and the mod URL.")}
                if os.path.getsize(dest) == 0:
                    os.unlink(dest)
                    return {"ok": False, "message": "Downloaded " + mod["name"] + " but the file is empty. Check the mod URL."}
            else:
                zip_path = os.path.join(tempfile.gettempdir(), mod["id"] + ".zip")
                ok, msg = _download(url, zip_path)
                if not ok:
                    if os.path.exists(zip_path):
                        os.unlink(zip_path)
                    return {"ok": False, "message": "Download failed for " + mod["name"] + ": " + (msg or "network error. Check your connection and the mod URL.")}
                with zipfile.ZipFile(zip_path, "r") as zf:
                    for name in zf.namelist():
                        if name.lower().endswith(".dll"):
                            zf.extract(name, plugins_dir)
                os.unlink(zip_path)
            installed = list(settings.get("installed_mods", []))
            if mod["id"] not in [m.get("id") for m in installed]:
                installed.append({"id": mod["id"], "name": mod["name"], "version": mod["version"]})
                settings["installed_mods"] = installed
                save_settings(settings)
            return {"ok": True, "message": "Installed " + mod["name"]}
        except Exception as e:
            return {"ok": False, "message": "Install failed: " + str(e)}

    def _remove_mod(self, mod_id):
        installed = list(settings.get("installed_mods", []))
        before = len(installed)
        installed = [m for m in installed if m.get("id") != mod_id]
        if len(installed) == before:
            return {"ok": False, "message": "Mod was not installed."}
        settings["installed_mods"] = installed
        save_settings(settings)
        return {"ok": True, "message": "Removed mod"}

    def _launch_game(self):
        game_dir = detect_game_dir()
        if not game_dir:
            return {"ok": False, "message": "Game not installed. Download it first."}
        exe_path = os.path.join(game_dir, "Among Us.exe")
        if not os.path.exists(exe_path):
            return {"ok": False, "message": "Among Us.exe not found in game directory."}

        if _au_game_procs():
            return {"ok": False, "message": "Game is already running. Close it first before launching again."}
        global _last_launch_ts
        now = time.time()
        if now - _last_launch_ts < 5.0:
            return {"ok": False, "message": "Game is launching, wait a moment before launching again."}
        _last_launch_ts = now

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
