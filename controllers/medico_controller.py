from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect

from models.medico_model import Medico
from database import db

#crear blueprint
medico_bp = Blueprint(
    "medico_bp",
    __name__
)

#listar
@medico_bp.route("/medicos")
def index():

    medicos = Medico.query.all()

    return render_template(
        "medico/index.html",
        medicos=medicos
    )

#formulario
@medico_bp.route("/medicos/create")
def create():

    return render_template(
        "medico/create.html"
    )

#guardar
@medico_bp.route(
    "/medicos/store",
    methods=["POST"]
)
def store():

    medico = Medico(
        nombre=request.form["nombre"],
        especialidad=request.form["especialidad"],
        telefono=request.form["telefono"],
        correo=request.form["correo"]
    )

    db.session.add(medico)

    db.session.commit()

    return redirect("/medicos")

#editar
@medico_bp.route("/medicos/edit/<int:id>")
def edit(id):

    medico = Medico.query.get(id)

    return render_template(
        "medico/edit.html",
        medico=medico
    )

#actualizar
@medico_bp.route(
    "/medicos/update/<int:id>",
    methods=["POST"]
)
def update(id):

    medico = Medico.query.get(id)

    medico.nombre = request.form["nombre"]
    medico.especialidad = request.form["especialidad"]
    medico.telefono = request.form["telefono"]
    medico.correo = request.form["correo"]

    db.session.commit()

    return redirect("/medicos")

#eliminar
@medico_bp.route("/medicos/delete/<int:id>")
def delete(id):

    medico = Medico.query.get(id)

    db.session.delete(medico)

    db.session.commit()

    return redirect("/medicos")