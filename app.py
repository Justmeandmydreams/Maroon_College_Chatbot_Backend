from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import get_response

app = Flask(__name__)

# Allow frontend domain to access backend
CORS(app, resources={r"/chat": {"origins": "*"}})

@app.route("/")
def home():
    return "Maroon backend is running"

@app.route("/chat", methods=["POST", "OPTIONS"])
def chat():
    if request.method == "OPTIONS":
        return jsonify({"status": "ok"}), 200

    data = request.get_json()
    user_message = data.get("message", "")

    reply = get_response(user_message)

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)