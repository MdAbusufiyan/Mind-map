from flask import Flask, send_from_directory
import webbrowser
import threading
import os

HOST = "127.0.0.1"
PORT = 8765

WEB_FOLDER = os.path.join(os.path.dirname(__file__), "web")

app = Flask(__name__, static_folder=WEB_FOLDER)

@app.route("/")
def index():
    return send_from_directory(WEB_FOLDER, "Mindmap.html")


@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(WEB_FOLDER, path)


def open_browser():
    webbrowser.open(f"http://{HOST}:{PORT}")

if __name__ == "__main__":
    threading.Timer(1.0, open_browser).start()

    app.run(
        host=HOST,
        port=PORT,
        debug=False,
        use_reloader=False
    )