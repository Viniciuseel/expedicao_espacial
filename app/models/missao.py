from app import db
from datetime import datetime

class Mission(db.Model):
    __tablename__ = "missoes"  
    __table_args__ = {'sqlite_autoincrement': True}

    id = db.Column(db.Integer,primary_key=True)
    nome_missao = db.Column(db.String(255)) 
    data_lancamento = db.Column(db.Date)
    destino = db.Column(db.String(255), nullable = False)
    tripulacao = db.Column(db.String) 
    carga_util = db.Column(db.String)
    duracao = db.Column(db.DateTime)
    custo = db.Column(db.Numeric)
    status = db.Column(db.String)
    status_detalhado = db.Column(db.Text)

    def __init__(self, nome_missao, data_lancamento, destino,  tripulacao , carga_util, duracao , custo, status, status_detalhado):
        self.nome_missao = nome_missao
        self.data_lancamento = data_lancamento
        self.destino = destino
        self.tripulacao = tripulacao
        self.carga_util = carga_util
        self.duracao = duracao
        self.custo = custo
        self.status = status
        self.status_detalhado = status_detalhado


    def buscarMissao(self, id):
        try:
            missoes = db.session.query(Mission).filter(Mission.id==id).first()
            return missoes
        except Exception as e:
            print(e)
    
    def listarMissao(self):
        try:
            missoes = db.session.query(Mission).order_by(Mission.data_lancamento.desc()).all()
            return missoes
        except  Exception as e:
            print(e)

    def listarPorData(self, dataInicial, dataFinal):
        try:
            missoes = db.session.query(Mission).filter((Mission.data_lancamento >= dataInicial) & (Mission.data_lancamento <= dataFinal)).order_by(Mission.data_lancamento.desc()).all()
            return missoes
        
        except Exception as e:
            print(e)
    
    def criarMissao(self, nome_missao, data_lancamento, destino,  tripulacao , carga_util, duracao , custo, status, status_detalhado ):
        try:
            add_banco = Mission(nome_missao, data_lancamento, destino, tripulacao, carga_util, duracao, custo, status, status_detalhado)
            print(add_banco)
            db.session.add(add_banco)
            db.session.commit()
        except Exception as e:
            print(e)
    
    def atualizarMissao(self, id, updated_data):
        try:
            db.session.query(Mission).filter(Mission.id==id).update(updated_data)
            db.session.commit()      
        except Exception as e:
            print(e)
    
    def deletarMissao(self, id):
        try:
            db.session.query(Mission).filter(Mission.id==id).delete()
            db.session.commit()
        except Exception as e:
            print(e)
    
   