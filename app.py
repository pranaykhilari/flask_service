from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Database connectivity
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://entercoms:tudip@123@localhost:5432/entercoms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# We define model in Models package. Below import statement is unused but it will tell flask-migrate to find
# models in models package.
import models

# Set the url configuration using blueprint
from urls import routes

app = routes(app)

if __name__ == '__main__':
    app.run(debug=True)


