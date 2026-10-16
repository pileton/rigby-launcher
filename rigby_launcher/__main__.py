#!/usr/bin/env python3
import subprocess
import sys
import threading
import time
from http.server import HTTPServer
from urllib.parse import urlparse

from rigby_launcher.server import APIHandler, _prefetch_icons

try:
    import gi
    gi.require_version("Gtk", "3.0")
    gi.require_version("WebKit2", "4.1")
    from gi.repository import Gtk, WebKit2
except Exception:
    Gtk = WebKit2 = None

BIND_HOST = "127.0.0.1"


def _find_port(start):
    for port in range(start, start + 100):
        try:
            s = HTTPServer((BIND_HOST, port), APIHandler)
            return port, s
        except OSError:
            continue
    raise RuntimeError("no available port found")


def _make_policy_handler(app_host):
    local_hosts = {"127.0.0.1", "localhost", app_host or ""}

    def on_decide_policy(webview, decision, decision_type, navigation_action=None):
        uri = None
        try:
            if navigation_action is not None:
                req = navigation_action.get_request()
                uri = req.get_uri() if req else None
        except Exception:
            uri = None
        if not uri:
            try:
                uri = decision.get_navigation_action().get_request().get_uri()
            except Exception:
                try:
                    uri = decision.get_request().get_uri()
                except Exception:
                    uri = None
        if uri and uri.startswith(("http://", "https://")):
            host = urlparse(uri).hostname
            if host and host not in local_hosts:
                try:
                    subprocess.Popen(["xdg-open", uri],
                                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                except Exception:
                    pass
                try:
                    decision.ignore()
                except Exception:
                    pass
                return True
        return False

    return on_decide_policy


def main():
    port, server = _find_port(8765)
    app_host = server.socket.getsockname()[0]
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    threading.Thread(target=_prefetch_icons, daemon=True).start()

    if sys.platform == "win32":
        _open_windows(port)
    else:
        try:
            if WebKit2 is None:
                raise RuntimeError("webkit not available")
            win = Gtk.Window.new(Gtk.WindowType.TOPLEVEL)
            win.set_title("Rigby Launcher")
            win.set_default_size(900, 620)
            win.set_position(Gtk.WindowPosition.CENTER)
            win.set_resizable(True)

            webview = WebKit2.WebView.new()
            webview.connect("decide-policy", _make_policy_handler(app_host))
            webview.load_uri(f"http://{BIND_HOST}:{port}")
            settings = webview.get_settings()
            settings.set_enable_developer_extras(False)
            win.add(webview)

            win.connect("destroy", lambda w: Gtk.main_quit())
            win.show_all()
            Gtk.main()

        except Exception as e:
            print(f"GTK unavailable ({e}), trying pywebview...")
            _open_native(port)


def _open_windows(port):
    try:
        import webview
        webview.create_window("Rigby Launcher", f"http://{BIND_HOST}:{port}", width=900, height=620, resizable=True)
        webview.start()
    except ImportError:
        import webbrowser
        webbrowser.open(f"http://{BIND_HOST}:{port}")
        while True:
            time.sleep(1)


def _open_native(port):
    try:
        import webview
        webview.create_window("Rigby Launcher", f"http://{BIND_HOST}:{port}", width=900, height=620, resizable=True)
        webview.start()
    except ImportError:
        import webbrowser
        print("Opening in browser...")
        webbrowser.open(f"http://{BIND_HOST}:{port}")
        while True:
            time.sleep(1)


if __name__ == "__main__":
    main()
