from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_marshmallow import Marshmallow

#Inicializando la app
app = Flask (__name__)

#Instanciar con la aplicación
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Crear tabla de estudiantes
class tbl_estudiantes (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cedula = db.Column(db.String(10), unique=True)
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    edad = db.Column(db.Integer)
    correo_electronico = db.Column(db.String(100))
    genero = db.Column(db.String(100))
    
    def __init__(self, cedula, nombre, apellido, edad, correo_electronico, genero):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.correo_electronico = correo_electronico
        self.genero = genero
               
db.create_all()   

#----------ESQUEMA----------#
class EstudiantesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'cedula', 'nombre', 'apellido', 'edad', 'correo electronico', 'genero')
        
estudiante_schema = EstudiantesSchema()
estudiantes_schema = EstudiantesSchema(many=True)