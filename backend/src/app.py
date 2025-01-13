from flask import Flask
from src.database import init_db
from src.routes import register_routes

app = Flask(__name__)
app.config.from_object("src.config.Config")

# Inicializáljuk az adatbázist
init_db(app)

# Regisztráljuk az API útvonalakat
register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
