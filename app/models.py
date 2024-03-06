#necesitamos a SQLAlchem: 
#definir  los atributos de objeto
#pero con tipos trauciobles a SQL y mysql
from app import db
from datetime import datetime

class Medico (db.Model):
    
    __tablename__ = "medicos"
    id  = db.Column(db.Integer , primary_key = True)
    nombre = db.Column(db.String(120), nullable = True)
    apellido = db.Column(db.String(120), nullable = True)
    tipo_identificacion = db.Column(db.String(4), nullable = True)
    numero_identificacion = db.Column(db.Integer)
    registro_medico = db.Column(db.Integer)
    especialidad = db.Column(db.String(50))
    
    citas = db.relationship('Cita' , backref = 'medico')
    
class Paciente (db.Model):
    
    __tablename__ = "pacientes"
    id  = db.Column(db.Integer , primary_key = True)
    nombre = db.Column(db.String(120), nullable = True)
    apellido = db.Column(db.String(120), nullable = True)
    tipo_identificacion = db.Column(db.String(4), nullable = True)
    numero_identificacion = db.Column(db.Integer)
    altura = db.Column(db.Integer)
    tipo_sangre = db.Column(db.String(2))
    
    citas = db.relationship('Cita' , backref = 'paciente')
    
class Consultorio (db.Model):
    
    __tablename__ = "consultorios"
    id  = db.Column(db.Integer , primary_key = True)
    numero = db.Column(db.Integer)
    
    citas = db.relationship('Cita' , backref = 'consultorio')
    
class Cita (db.Model):
    __tablename__ = "citas"
    id  = db.Column(db.Integer , primary_key = True)
    fecha = db.Column(db.DateTime, default = datetime.utcnow)
    paciente_id = db.Column(db.Integer, db.ForeignKey("pacientes.id"))
    medico_id = db.Column(db.Integer, db.ForeignKey("medicos.id"))
    consultorio_id = db.Column(db.Integer, db.ForeignKey("consultorios.id"))
    valor = db.Column(db.Integer)    
    
    
    """
    from app import app, db
    from datetime import datetime
    app.app_context().push() 
    from app.models import Medico, Paciente, Consultorio, Cita
    
    med1 = Medico(nombre = "Pablo", apellido = "Rivas", tipo_identificacion = "CC", numero_identificacion = 1116548, registro_medico = 2409, especialidad = "Patologo") 
    med2 = Medico(nombre = "Carlos", apellido = "Vargas", tipo_identificacion = "CC", numero_identificacion = 8372910, registro_medico = 2312, especialidad = "Pediatra") 
    med3 = Medico(nombre = "Laura", apellido = "Lopez", tipo_identificacion = "CC", numero_identificacion = 1725638, registro_medico = 1823, especialidad = "Cardiologa") 
    pac1 = Paciente(nombre = "Natalia", apellido = "Jimenez", tipo_identificacion = "CC", numero_identificacion = "187812", altura = 165, tipo_sangre = "O+")
    pac2 = Paciente(nombre = "Jhojan", apellido = "Beltran", tipo_identificacion = "CC", numero_identificacion = "127862", altura = 172, tipo_sangre = "A+")
    pac3 = Paciente(nombre = "Pedro", apellido = "Guevara", tipo_identificacion = "CC", numero_identificacion = "982398", altura = 162, tipo_sangre = "A+")
    con1 = Consultorio(numero = 1) 
    con2 = Consultorio(numero = 2)
    con3 = Consultorio(numero = 3)
    cit1 = Cita(fecha = fecha1, paciente = pac1, medico = med3, consultorio = con2, valor = 10) 
    cit2 = Cita(fecha = fecha3, paciente = pac3, medico = med2, consultorio = con1, valor = 20) 
    fecha1 = datetime(2024,7,14,12,45,0)
    fecha2 = datetime(2024,9,9,16,15,0)
    fecha3 = datetime(2024,11,2,7,0,0) 
    db.session.add()
    db.session.commit()
    
    #traer objeto por id
    med1 = Medico.query.get(1)
    
    #muestra todas los valores citas
    citas = Cita.query.all():
    citas
    
    #cast: conversion de un tipo de dato a otro
    
    #realizar un "for"
    for ci in Cita.query.all():
        print("fecha:" + str(ci.fecha))
        print("fecha:" + str(ci.fecha)+"|Paciente:" + str(ci.paciente.numero_identificacion) + ",paciente nombre:" + ci.paciente.nombre + " " + ci.paciente.apellido) 
        print("fecha:" + str(ci.fecha)+"|Paciente:" + str(ci.paciente.numero_identificacion) + ",paciente nombre:" + ci.paciente.nombre + " " + ci.paciente.apellido + "valor cita:" + str(ci.valor))
        #RESULTADO
        fecha:2024-07-14 12:45:00|Paciente:187812,paciente nombre:Natalia Jimenezvalor cita:10
        fecha:2024-11-02 07:00:00|Paciente:982398,paciente nombre:Pedro Guevaravalor cita:20
    #ACTIVIDAD#
    paciente: numero_identificacion, nombres, apellidos
    medico: registro_medico
    consultorio: numero
    cita: agregar +1 atributo
    """