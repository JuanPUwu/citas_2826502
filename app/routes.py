from . import app, db
from .models import Medico, Paciente, Consultorio, Cita
from flask import render_template, request, flash, redirect, url_for, Flask
from datetime import datetime

#definir ruta para listado de medicos
@app.route("/medicos")
def get_all_medicos():
    medicos = Medico.query.all()
    return render_template("medicos.html",
                           medicos = medicos)

#definir ruta para listado de pacientes
@app.route("/pacientes")
def get_all_pacientes():
    pacientes = Paciente.query.all()
    return render_template("pacientes.html",
                           pacientes = pacientes)

#definir ruta para lista de consultorios
@app.route("/consultorios")
def get_all_consultorios():
    consultorios = Consultorio.query.all()
    return render_template("consultorios.html",
                           consultorios = consultorios)

#definir ruta para lista de citas
@app.route("/citas")
def get_all_citas():
    citas = Cita.query.all()
    return render_template("citas.html",
                           citas = citas)

#
#
#
#
#

#crear ruta para traer medicos con metodo "get"
@app.route("/medicos/<int:id>")
def get_medico_by_id(id):
        #return "id del medico: " + str(id)
        #traer medico por id utilizando la entidad Medico
        medico = Medico.query.get(id)
        #y meterlo a una lista
        return render_template("medico.html",
                               med = medico)

#crear ruta para traer pacientes con metodo "get"
@app.route("/pacientes/<int:id>")
def get_paciente_by_id(id):
    paciente = Paciente.query.get(id)
    return render_template("paciente.html",
                           pac = paciente)


#crear ruta para traer consultorio con metodo "get"
@app.route("/consultorios/<int:id>")
def get_consultorio_by_id(id):
    consultorio = Consultorio.query.get(id)
    return render_template("consultorio.html",
                           con = consultorio)

#crear ruta para traer cita con metodo "get"
@app.route("/citas/<int:id>")
def get_cita_by_id(id):
    cita = Cita.query.get(id)
    return render_template("cita.html",
                           cit = cita)

#
#
#
#
#

#CREAR RUTA PARA CREAR NUEVO MEDICO
@app.route("/medicos/create", methods = ["GET","POST"])
def create_medico():
    #mostrar el formulario en metodo "get"
    if(request.method == "GET" ):
        #el usuario ingreso con navegador con http://localhost:5000/medicos/create
        especialidades = [
            "Seleccionar...",
            "Cardiologia",
            "Optometria",
            "Radiologia",
            "Pediatria",
            "Odontologia"
        ]
        return render_template("medico_form.html",
                            especialidades = especialidades)
    elif(request.method == "POST"):
        #se presiona guardar
        #   return request.form["es"]
        #cuando el usuario presiona el boton guardar
        #los datos del formulario viajan al servidor utilizando el metodo "post"
        #crea un objeto medico
        new_medico = Medico(nombre = request.form["nombre"],
                            apellido = request.form["apellido"],
                            tipo_identificacion = request.form["ti"],
                            numero_identificacion = request.form["ni"],
                            registro_medico = request.form["rm"],
                            especialidad = request.form["es"]
                            )
        #añadirlo a la sesion sqlalchemy
        db.session.add(new_medico)
        db.session.commit()
        return redirect("/medicos")


##CREAR RUTA PARA CREAR NUEVO PACIENTE
@app.route("/pacientes/create", methods = ["GET","POST"])
def create_paciente():
    if(request.method == "GET" ):
        tipo_sangre = [
            "Seleccionar...",
            "A+",
            "A-",
            "B+",
            "B-",
            "AB+",
            "AB-",
            "O+",
            "O-"
        ]
        return render_template("paciente_form.html",
                            tipo_sangre = tipo_sangre)
    elif(request.method == "POST"):
        new_paciente = Paciente(nombre = request.form["nombre"],
                            apellido = request.form["apellido"],
                            tipo_identificacion = request.form["ti"],
                            numero_identificacion = request.form["ni"],
                            altura = request.form["al"],
                            tipo_sangre = request.form["ts"]
                            )
        db.session.add(new_paciente)
        db.session.commit()
        return redirect("/pacientes")


#CREAR RUTA PARA CREAR NUEVO CONSULTORIO
@app.route("/consultorios/create", methods = ["GET","POST"])
def create_consultorio():
    if(request.method == "GET" ):
        numeros = [
            "Seleccionar...",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10"
        ]
        return render_template("consultorio_form.html",
                            numeros = numeros)
    elif(request.method == "POST"):
        new_consultorio = Consultorio(numero = request.form["numero"])
        db.session.add(new_consultorio)
        db.session.commit()
        return redirect("/consultorios")


#CREAR RUTA PARA CREAR NUEVA CITA
@app.route("/citas/create", methods = ["GET","POST"])
def create_cita():
    if(request.method == "GET" ):
        fecha = [
            datetime(2024,9,12,14,45,0),
            datetime(2024,8,8,15,15,0),
            datetime(2024,2,15,16,15,0),
            datetime(2024,1,28,8,45,0),
            datetime(2024,12,30,7,0,0),
        ]
        return render_template("citas_form.html",
                            citas = fecha)
    elif(request.method == "POST"):
        new_cita = Cita(fecha = request.form["fe"],
                        paciente_id = request.form["pi"],
                        medico_id = request.form["mi"],
                        consultorio_id = request.form["ci"],
                        valor = request.form["va"])
        db.session.add(new_cita)
        db.session.commit()
        return "Cita registrada"

#
#
#
#
#

#ACTUALIZAR DATOS MEDICOS
@app.route("/medicos/update/<int:id>", methods = ["POST", "GET"])
def update_medico(id):
    especialidades = [
            "Seleccionar...",
            "Cardiologia",
            "Optometria",
            "Radiologia",
            "Pediatria",
            "Odontologia"
        ]
    medico_update = Medico.query.get(id)
    if(request.method == "GET"):
        return render_template("medico_update.html",
                                medico_update = medico_update,
                                especialidades = especialidades)
    elif(request.method == "POST"):
        #ACTUALIZAR MEDICO CON DATOS DE FORMULARIO
        medico_update.nombre = request.form["nombre"]
        medico_update.apellido = request.form["apellido"]
        medico_update.tipo_identificacion = request.form["ti"]
        medico_update.numero_identificacion = request.form["ni"]
        medico_update.registro_medico = request.form["rm"]
        medico_update.especialidad = request.form["es"]
        db.session.commit()
        return redirect("/medicos")

@app.route("/medicos/delete/<int:id>")
def delete_medico(id):
    medico_delete = Medico.query.get(id)
    db.session.delete(medico_delete)
    db.session.commit()
    return redirect("/medicos")


#ACTUALIZAR DATOS CONSULTORIO
@app.route("/consultorios/update/<int:id>", methods = ["POST", "GET"])
def update_consultorio(id):
    numeros = [
            "Seleccionar...",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10"
        ]
    consultorio_update = Consultorio.query.get(id)
    if(request.method == "GET"):
        return render_template("consultorio_update.html",
                                consultorio_update = consultorio_update,
                                numeros = numeros)
    elif(request.method == "POST"):
        #ACTUALIZAR MEDICO CON DATOS DE FORMULARIO
        consultorio_update.numero = request.form["numero"]
        db.session.commit()
        return redirect("/consultorios")

@app.route("/consultorios/delete/<int:id>")
def delete_consultorio(id):
    consultorio_delete = Consultorio.query.get(id)
    db.session.delete(consultorio_delete)
    db.session.commit()
    return redirect("/consultorios")


#ACTUALIZAR DATOS PACIENTES
@app.route("/pacientes/update/<int:id>", methods = ["POST", "GET"])
def update_paciente(id):
    tipo_sangre = [
            "Seleccionar..."
            "A+",
            "A-",
            "B+",
            "B-",
            "AB+",
            "AB-",
            "O+",
            "O-"
        ]
    paciente_update = Paciente.query.get(id)
    if(request.method == "GET"):
        return render_template("paciente_update.html",
                                paciente_update = paciente_update,
                                tipo_sangre = tipo_sangre)
    elif(request.method == "POST"):
        #ACTUALIZAR MEDICO CON DATOS DE FORMULARIO
        paciente_update.nombre = request.form["nombre"]
        paciente_update.apellido = request.form["apellido"]
        paciente_update.tipo_identificacion = request.form["ti"]
        paciente_update.numero_identificacion = request.form["ni"]
        paciente_update.altura = request.form["al"]
        paciente_update.tipo_sangre = request.form["ts"]
        db.session.commit()
        return redirect("/pacientes")

@app.route("/pacientes/delete/<int:id>")
def delete_paciente(id):
    paciente_delete =Paciente.query.get(id)
    db.session.delete(paciente_delete)
    db.session.commit()
    return redirect("/pacientes")


