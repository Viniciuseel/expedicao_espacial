from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS 

#inicializando Flask
app = Flask(__name__)
CORS (app)
api = Api(app)

#configuração do banco de dados
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///missoes.sqlite3'
app.config ['SQLALCHEMY_TRACK_MODIFICATIONS']  = False
# criando instância do SQLALCHEMY e vinculando ao flask
db = SQLAlchemy(app)

from app.models.missao import Missao
with app.app_context():
    db.create_all()

from app.reso_missao import index, MissaoCreate, MissaoUpdate, MissaoDelete
api.add_resource(index,'/')
api.add_resource(index,'/Criar')
api.add_resource(index,'/Atualizar')
api.add_resource(index,'/Deletar')





