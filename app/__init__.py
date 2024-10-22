
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_restful import Api 
# from flask_cors import CORS

app = Flask(__name__)
# CORS(app)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///missoes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  = False
db = SQLAlchemy(app)

from app.models.missao import Mission
with app.app_context():
     db.create_all()

from app.view.reso_missao import MissionsListView, MissionsView
 
api.add_resource(MissionsListView,"/missoes/")
api.add_resource(MissionsView,"/missoes/<id>")
