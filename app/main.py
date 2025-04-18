from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')

def home():
    return jsonify({
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "ip": request.remote_addr if request.remote_addr else "Unknown"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


