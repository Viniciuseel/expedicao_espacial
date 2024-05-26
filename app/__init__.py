
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_restful import Api 
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///missoes.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  = False
db = SQLAlchemy(app)

from app.models.missao import Mission
with app.app_context():
     db.create_all()

from app.view.reso_missao import Index, MissionsView
api.add_resource(Index, "/missoes") 
api.add_resource(MissionsView,"/missions/<int:id>")