from flask import Flask, request, render_template, flash, jsonify, redirect, url_for
import json
import mysql.connector 
from mysql.connector import errorcode

# #CONEXION A BASE DE DATOS
# try:
#   cnx = mysql.connector.connect(user='root',password='',host='localhost',database='curso')
# except mysql.connector.Error as err:
#   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#     print("error de usuario o contraseña")
#   elif err.errno == errorcode.ER_BAD_DB_ERROR:
#     print("No existe la base de datos")
#   else:
#     print(err)
# else:
#   print('Conexion Exitosa')
#   cnx.close()

# cnx = mysql.connector.connect(user='root',password='',host='localhost',database='curso')
# mycursor = cnx.cursor()

app = Flask(__name__)

# @app.errorhandler(404)
# def page_not_found(err):
#     return render_template("notfound.html"), 404

@app.route('/')
def index():
    return render_template('/index.html')

@app.route("/search")
def search():  
    return render_template('/search.html')
  
@app.route("/contact")
def contact():  
    return render_template('/contact.html')

@app.route("/results",  methods = ['POST'])
def results():
    if request.method == 'POST':
        project = request.form.get('marca')
        print(project)
        
    return render_template('/results.html')

app.run()