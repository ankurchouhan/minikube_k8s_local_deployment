from flask import Flask
import requests
import os

app = Flask(__name__)

BACKEND_URL = os.environ.get("BACKEND_URL", "http://express-backend:3000")

@app.route("/")
def index():
    try:
        r = requests.get(f"{BACKEND_URL}/api/message", timeout=2)
        data = r.json()
        backend_message = data.get("message", "No message field in response")
    except Exception as e:
        backend_message = f"Error talking to backend: {e}"

    return f"""
    <html>
      <head><title>Flask + Express on Kubernetes</title></head>
      <body>
        <h1>Flask Frontend</h1>
        <p>This is served by the Flask frontend container.</p>
        <h2>Message from Express backend:</h2>
        <pre>{backend_message}</pre>
      </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
