from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/", methods=["POST"])
def check_urls():
    data = request.get_json()
    urls = data.get("urls", [])
    results = []

    for url in urls:
        try:
            r = requests.head(url, timeout=5)
            results.append({"url": url, "status": "up", "code": r.status_code})
        except Exception as e:
            results.append({"url": url, "status": "down", "error": str(e)})

    return jsonify(results)
