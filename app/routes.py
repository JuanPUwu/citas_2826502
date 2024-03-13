from . import app, db
from .models import Medico, Paciente, Consultorio, Cita
from flask import render_template, request
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


@app.route("/citas/<int:id>")
def get_cita_by_id(id):
    cita = Cita.query.get(id)
    return render_template("cita.html",
                           cit = cita)
    
    
    
    
#crear una ruta para crear nuevo medico
@app.route("/medicos/create", methods = ["GET","POST"])
def create_medico():
    #mostrar el formulario en metodo "get"
    if(request.method == "GET" ):
        #el usuario ingreso con navegador con http://localhost:5000/medicos/create
        especialidades = [
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
        return "Medico registrado"

#ruta para pacientes
@app.route("/pacientes/create", methods = ["GET","POST"])
def create_pacientes():
    if(request.method == "GET" ):
        tipo_sangre = [
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
        return "Paciente registrado"


#crear una ruta para crear un nuevo consultorio
@app.route("/consultorios/create", methods = ["GET","POST"])
def create_consultorios():
    if(request.method == "GET" ):
        numeros = [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9"
        ]
        return render_template("consultorio_form.html",
                            numeros = numeros)


    elif(request.method == "POST"):
        new_consultorio = Consultorio(numero = request.form["nu"])
        db.session.add(new_consultorio)
        db.session.commit()
        return "Consultorio registrado"


#crear una ruta para crear un nuevo cita
@app.route("/citas/create", methods = ["GET","POST"])
def create_citas():
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
        return "Cita registrado"