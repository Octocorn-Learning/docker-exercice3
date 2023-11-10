from flask import Flask
from flask_cors import CORS
from flask_mysqldb import MySQL
app = Flask(__name__)
CORS(app)
mysql = MySQL(app)

from app import routes

app.config['MYSQL_HOST']='db'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='root'
app.config['MYSQL_DB']='beer'
