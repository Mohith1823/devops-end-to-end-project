from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>DevOps CI/CD Project</h1>
    <p>Welcome to Flask Application</p>
    """

@app.route("/health")
def health():
    return {
        "status": "UP",
        "application": "Flask DevOps Project"
    }

@app.route("/version")
def version():
    return {
        "version": "1.0.0"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
