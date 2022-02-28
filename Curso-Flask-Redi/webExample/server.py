from flask import Flask, render_template, request
import flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("form.html")

@app.route('/procesa', methods=['POST'])
def procesa():
    nombre   = request.form["nombre"]

    return "Tu nombres es: " + nombre

app.run(debug=True)