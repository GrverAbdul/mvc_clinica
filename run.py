from flask import Flask
from database import db

#controladores
from controllers.medico_controller import medico_bp
from controllers.paciente_controller import paciente_bp
from controllers.consulta_controller import consulta_bp
from controllers.auth_controller import auth_bp

app = Flask(__name__)

#configuracion de sqlalchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///clinica.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#clave secreta
app.secret_key = "clinica_secret"

#inicializar db
db.init_app(app)

#registrar blueprints
app.register_blueprint(medico_bp)
app.register_blueprint(paciente_bp)
app.register_blueprint(consulta_bp)
app.register_blueprint(auth_bp)

#crear tablas
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return """
    <h1>sistema clinico mvc</h1>

    <a href='/medicos'>medicos</a><br>
    <a href='/pacientes'>pacientes</a><br>
    <a href='/consultas'>consultas</a><br>
    """

if __name__ == "__main__":
    app.run(debug=True)