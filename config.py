from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# config.py
USER = "root"
PASSWORD = ""
HOST = "localhost"
DATABASE = "cursePython"

# Configuracion de la base de datos
DATABASE_URI = f'mysql+pymysql://{USER} :{PASSWORD}@{HOST}/{DATABASE}'
db = SQLAlchemy()

