from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Nutrilog API está online! 🍎"

if __name__ == "__main__":
    # O Render fornece a porta automaticamente na variável de ambiente PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)