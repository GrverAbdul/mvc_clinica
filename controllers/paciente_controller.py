from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect

from database import db
from models.paciente_model import Paciente

#crear blueprint
paciente_bp = Blueprint(
    "paciente_bp",
    __name__
)

#listar
@paciente_bp.route("/pacientes")
def index():

    pacientes = Paciente.query.all()

    return render_template(
        "paciente/index.html",
        pacientes=pacientes
    )

#formulario
@paciente_bp.route("/pacientes/create")
def create():

    return render_template(
        "paciente/create.html"
    )

#guardar
@paciente_bp.route(
    "/pacientes/store",
    methods=["POST"]
)
def store():

    paciente = Paciente(
        nombre=request.form["nombre"],
        edad=request.form["edad"],
        direccion=request.form["direccion"],
        telefono=request.form["telefono"]
    )

    db.session.add(paciente)

    db.session.commit()

    return redirect("/pacientes")

#editar
@paciente_bp.route("/pacientes/edit/<int:id>")
def edit(id):

    paciente = Paciente.query.get(id)

    return render_template(
        "paciente/edit.html",
        paciente=paciente
    )

#actualizar
@paciente_bp.route(
    "/pacientes/update/<int:id>",
    methods=["POST"]
)
def update(id):

    paciente = Paciente.query.get(id)

    paciente.nombre = request.form["nombre"]
    paciente.edad = request.form["edad"]
    paciente.direccion = request.form["direccion"]
    paciente.telefono = request.form["telefono"]

    db.session.commit()

    return redirect("/pacientes")

#eliminar
@paciente_bp.route("/pacientes/delete/<int:id>")
def delete(id):

    paciente = Paciente.query.get(id)

    db.session.delete(paciente)

    db.session.commit()

    return redirect("/pacientes")