from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    # Single-page landing site: every path serves the landing page,
    # the same fallback pattern nestarr.com uses.
    return send_from_directory("public", "index.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
