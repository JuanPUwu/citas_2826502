from . import app
from .models import Medico, Paciente, Consultorio, Cita
from flask import render_template

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