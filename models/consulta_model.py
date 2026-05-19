from database import db

#modelo consulta
class Consulta(db.Model):

    __tablename__ = "consultas"

    id = db.Column(db.Integer, primary_key=True)

    fecha = db.Column(db.String(20), nullable=False)

    diagnostico = db.Column(db.Text, nullable=False)

    tratamiento = db.Column(db.Text, nullable=False)

    #llave foranea medico
    id_medico = db.Column(
        db.Integer,
        db.ForeignKey("medicos.id")
    )

    #llave foranea paciente
    id_paciente = db.Column(
        db.Integer,
        db.ForeignKey("pacientes.id")
    )

    #relaciones
    medico = db.relationship(
        "Medico",
        back_populates="consultas"
    )

    paciente = db.relationship(
        "Paciente",
        back_populates="consultas"
    )