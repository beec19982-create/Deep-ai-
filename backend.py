
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from openai import OpenAI

app = Flask(__name__)
CORS(app)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/api/ask", methods=["POST"])
def ask_ai():
    data = request.json
    prompt = data.get("prompt")

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return jsonify({"response": response.output_text})

@app.route("/")
def home():
    return "AI Super App Backend Running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
