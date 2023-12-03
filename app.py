from flask import Flask, render_template, url_for
import socket
import logging
import gunicorn

app = Flask(__name__)

@app.route("/", methods=["GET"])
def render_home():
    return ("<div style='display: flex; height: 100vh; flex-direction: column; justify-content: center; align-items: center;'>"
            f"<h1>Welcome to Test Dockerized Nginx Flask App</h1>"
            f"<h2>You are connecting flask container {socket.gethostbyaddr(socket.gethostname())} {socket.gethostname()} </h2>"
            "</div>")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)