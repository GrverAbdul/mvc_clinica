from database import db

#modelo medico
class Medico(db.Model):

    __tablename__ = "medicos"

    id = db.Column(db.Integer, primary_key=True)

    nombre = db.Column(db.String(100), nullable=False)

    especialidad = db.Column(db.String(100), nullable=False)

    telefono = db.Column(db.String(20))

    correo = db.Column(db.String(100))

    #relacion uno a muchos
    consultas = db.relationship(
        "Consulta",
        back_populates="medico",
        cascade="all, delete-orphan"
    )