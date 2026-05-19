from database import db

#modelo paciente
class Paciente(db.Model):

    __tablename__ = "pacientes"

    id = db.Column(db.Integer, primary_key=True)

    nombre = db.Column(db.String(100), nullable=False)

    edad = db.Column(db.Integer)

    direccion = db.Column(db.String(200))

    telefono = db.Column(db.String(20))

    #relacion uno a muchos
    consultas = db.relationship(
        "Consulta",
        back_populates="paciente",
        cascade="all, delete-orphan"
    )