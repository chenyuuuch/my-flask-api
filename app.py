from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from the cloud!"

if __name__ == "__main__":
    app.run()
