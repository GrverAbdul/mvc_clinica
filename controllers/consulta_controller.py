from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect

from database import db

from models.consulta_model import Consulta
from models.medico_model import Medico
from models.paciente_model import Paciente

#crear blueprint
consulta_bp = Blueprint(
    "consulta_bp",
    __name__
)

#listar consultas
@consulta_bp.route("/consultas")
def index():
    #obtener fecha
    fecha = request.args.get("fecha")
    #filtrar consultas
    if fecha:
        consultas = Consulta.query.filter_by(fecha=fecha).all()
    else:
        consultas = Consulta.query.all()

    return render_template(
        "consulta/index.html",
        consultas=consultas
    )

#formulario
@consulta_bp.route("/consultas/create")
def create():

    medicos = Medico.query.all()

    pacientes = Paciente.query.all()

    return render_template(
        "consulta/create.html",
        medicos=medicos,
        pacientes=pacientes
    )

#guardar
@consulta_bp.route(
    "/consultas/store",
    methods=["POST"]
)
def store():

    consulta = Consulta(
        fecha=request.form["fecha"],
        diagnostico=request.form["diagnostico"],
        tratamiento=request.form["tratamiento"],
        id_medico=request.form["id_medico"],
        id_paciente=request.form["id_paciente"]
    )

    db.session.add(consulta)

    db.session.commit()

    return redirect("/consultas")

#eliminar
@consulta_bp.route("/consultas/delete/<int:id>")
def delete(id):

    consulta = Consulta.query.get(id)

    db.session.delete(consulta)

    db.session.commit()

    return redirect("/consultas")