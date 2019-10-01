from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api
from flask_cors import CORS

app = Flask(__name__)

# Database connectivity
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://entercoms:tudip@123@localhost:5432/entercoms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '02814be6738fa76067457ec6b5af7b46512ded6f8202b77e'

db = SQLAlchemy(app)

# Handle the cross site request error
cors = CORS(app)

# We define model in Models package. Below import statement is unused but it will tell flask-migrate to find
# models in models package.

import models

# Set the url configuration using blueprint
from urls import routes

app = routes(app)

api = Api(app, version='1.0', title='Sample API',
          description='A sample API'
          )

if __name__ == '__main__':
    app.run(debug=True)
