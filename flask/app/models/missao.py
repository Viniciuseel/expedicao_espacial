from app import db

from datetime import datetime

class Mission(db.Model):
    __tablename__ = "missoes"  
    __table_args__ = {'sqlite_autoincrement': True}

    id = db.Column(db.Integer,primary_key=True)
    nome_missao = db.Column(db.String(255)) 
    data_lancamento = db.Column(db.Integer)
    data_final = db.Column(db.Integer)
    destino = db.Column(db.String(255), nullable = False)
    tripulacao = db.Column(db.String(255)) 
    carga_util = db.Column(db.String(255))
    duracao = db.Column(db.Integer)
    custo = db.Column(db.Float)
    status = db.Column(db.String(120))

    def __init__(self, nome_missao, data_lancamento, data_final , destino,  tripulacao , carga_util, duracao , custo, status):
        self.nome_missao = nome_missao
        self.data_lancamento = data_lancamento
        self.data_final = data_final
        self.destino = destino
        self.tripulacao = tripulacao
        self.carga_util = carga_util
        self.duracao = duracao
        self.custo = custo
        self.status = status


    def criar_missao(self, nome_missao, data_lancamento, data_final , destino,  tripulacao , carga_util, duracao , custo, status ):
        try:
            add_banco = Mission(self, nome_missao, data_lancamento, data_final , destino,  tripulacao , carga_util, duracao , custo, status)
            print(add_banco)
            db.session.add(add_banco)
            db.session.commit()
        except Exception as e:
            print(e)
    
    def atualizar_missao(self, nome_missao, data_lancamento, data_final , destino,  tripulacao , carga_util, duracao , custo, status ):
        try:
            db.session.query(Mission).filter(Mission.id==id).update({"nome_missao":nome_missao, "destino":destino,"data_lancamento":data_lancamento, "tripulacao":tripulacao, 
                                                                     "carga_util":carga_util, "status":status, "data_final": data_final, "duracao":duracao, "custo":custo})
            db.session.commit()      
        except Exception as e:
            print(e)
    
    def deletar_missao(self, id):
        try:
            db.session.query(Mission).filter(Mission.id==id).delete()
            db.session.commit()
        except Exception as e:
            print(e)
    
   