from . import app, db
from .models import Medico, Paciente, Consultorio, Cita
from flask import render_template, request

#definir ruta para listado de medicos
@app.route("/medicos")
def get_all_medicos():
    medicos = Medico.query.all()
    return render_template("medicos.html",medicos = medicos)

#definir ruta para listado de pacientes
@app.route("/pacientes")
def get_all_pacientes():
    pacientes = Paciente.query.all()
    return render_template("pacientes.html",pacientes = pacientes)

#definir ruta para lista de consultorios
@app.route("/consultorios")
def get_all_consultorios():
    consultorios = Consultorio.query.all()
    return render_template("consultorios.html",consultorios = consultorios)

#definir ruta para lista de citas
@app.route("/citas")
def get_all_citas():
    citas = Cita.query.all()
    return render_template("citas.html",citas = citas)

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


    