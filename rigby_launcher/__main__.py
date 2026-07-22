import sys
import threading
import time
from http.server import HTTPServer

from rigby_launcher.server import APIHandler


def main():
    port = 8765
    server = HTTPServer(("127.0.0.1", port), APIHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    if sys.platform == "win32":
        _open_windows(port)
    else:
        try:
            import gi
            gi.require_version("Gtk", "3.0")
            gi.require_version("WebKit2", "4.1")
            from gi.repository import Gtk, WebKit2

            win = Gtk.Window.new(Gtk.WindowType.TOPLEVEL)
            win.set_title("Rigby Launcher")
            win.set_default_size(900, 620)
            win.set_position(Gtk.WindowPosition.CENTER)
            win.set_resizable(True)

            webview = WebKit2.WebView.new()
            webview.load_uri(f"http://127.0.0.1:{port}")
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
        webview.create_window("Rigby Launcher", f"http://127.0.0.1:{port}", width=900, height=620, resizable=True)
        webview.start()
    except ImportError:
        import webbrowser
        webbrowser.open(f"http://127.0.0.1:{port}")
        while True:
            time.sleep(1)


def _open_native(port):
    try:
        import webview
        webview.create_window("Rigby Launcher", f"http://127.0.0.1:{port}", width=900, height=620, resizable=True)
        webview.start()
    except ImportError:
        import webbrowser
        print("Opening in browser...")
        webbrowser.open(f"http://127.0.0.1:{port}")
        while True:
            time.sleep(1)


if __name__ == "__main__":
    main()
