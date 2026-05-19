from database import db

#modelo usuario
class Usuario(db.Model):

    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(
        db.String(50),
        nullable=False
    )

    password = db.Column(
        db.String(100),
        nullable=False
    )