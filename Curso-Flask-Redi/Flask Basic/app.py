from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/home")
def home():
    return "Esta es la pagina de home"

if __name__ == "__main__":
    app.run()