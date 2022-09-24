from tbl_estudiantes import*

class DevelopmentConfig():
    DEBUG = True #---para tener activo el modo debug, permitiendo actualizar los cambios sin tener que ejecutar de nuevo---#
    
    #cadena de conexión al servidor de datos.
    app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root@localhost:3306/examen_p2'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #para no presentar los warnning
    
    
config = {
    'development': DevelopmentConfig
}