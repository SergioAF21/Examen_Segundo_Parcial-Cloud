#importar librerias y clases
from flask import jsonify, request
from tbl_estudiantes import* 
from config import*

#-----------PAGINA INICIAL--------#
@app.route('/', methods=['GET'])
def index():
    return jsonify({'mensaje': 'Esto es una API'})


#---------CREAR TABLA METODO GET-----------#
@app.route('/crear_tabla', methods=['GET'])
def crear_tabla ():
    try:
        db.create_all() 
        return jsonify({'mensaje': "Tabla creada.", 'exito': True})
    
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


#--------------------AGREGAR ESTUDIANTE METODO POST--------------------------------#
@app.route('/agregar_estudiante', methods=['POST'])
def agregar_estudiante():
    try:
        cedula= request.json['cedula']
        nombre = request.json['nombre']
        apellido = request.json['apellido']
        edad = request.json['edad']
        correo_electronico = request.json['correo electronico']
        genero = request.json['genero']
        
        new_add = tbl_estudiantes(cedula, nombre, apellido, edad, correo_electronico, genero) 
        db.session.add(new_add)
        db.session.commit()  # Confirma la acción de inserción.
        return jsonify({'mensaje': "Estudiante agregado.", 'exito': True})
    
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


#----------LISTA DE ESTUDIANTES METODO GET--------#
@app.route('/lista_estudiantes', methods =['GET'])
def lista_estudiantes():
    try:
        list_estudiantes= tbl_estudiantes.query.all()
        result = estudiantes_schema.dump(list_estudiantes)
        return jsonify(result)
    
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})

#---------BUSCAR ESTUDIANTE METODO GET-------------#
@app.route('/buscar_estudiante/<apellido>', methods=['GET'])
def buscar_estudiante(apellido):
    try:
        buscar = tbl_estudiantes.query.get(apellido)
        return estudiante_schema.jsonify(buscar)
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})

#---------EDITAR DATOS DE ESTUDIANTE METODO PUT---------#
@app.route('/editar_estudiante/<id>', methods=['PUT'])
def editar_estudiante(id):
    actualizar = tbl_estudiantes.query.get(id)
        
    cedula= request.json['cedula']
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    edad = request.json['edad']
    correo_electronico = request.json['correo electronico']
    genero = request.json['genero']
        
    actualizar.cedula = cedula
    actualizar.nombre = nombre
    actualizar.apellido = apellido
    actualizar.edad = edad
    actualizar.correo_electronico = correo_electronico
    actualizar.genero = genero
    
    db.session.commit()
    return jsonify({'mensaje': "Datos del Estudiante actualizados", 'exito': True})

#-------------ELIMINAR ESTUDIANTE METODO DELETE----------#
@app.route('/eliminar_estudiante/<id>', methods=['DELETE'])
def eliminar_estudiante(id):
    try:
        new = tbl_estudiantes.query.get(id)
        db.session.delete(new)
        db.session.commit()
        return jsonify({'mensaje': "Estudiante eliminado.", 'exito': True})

    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


#---------CREACIÓN DE MÉTODO "PAGINA NO ENCONTRADA-----------#
def pagina_no_encontrada(error): 
    return "<h1>Página no encontrada</h1>", 404 #retorna un mensaje, al reconocer el error 404.

    
#Mientras se ejecuta la app
if __name__== '__main__':
    app.config.from_object(config['development'])
    
    app.register_error_handler(404, pagina_no_encontrada) #Registro de error, al no encontrar la pagina.
    
    app.run() # se usa para correr la aplicación.