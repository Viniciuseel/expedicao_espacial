from app import db

class Missao(db.Model):
    __tablename__ = 'missao'
    __table_args__ = {'sqlite_autoincrement': True}
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50))
    data = db.Column(db.Integer)
    destino = db.Column(db.String(50))
def __init__(self, nome, data):
        self.nome = nome
        self.data = data

def save_missao(self,nome,data):
    try:
            add_banco=Missao(nome,data)
            print (add_banco)

            db.session.add(add_banco)
            db.session.commit()
            
    except Exception as e: 
            print(e)

def update_missao(self,id,name,data):
    try:
            db.session.query(Missao).filter(Missao.id==id).update({"name":name,"data":data})
            db.session.commit()

    except Exception as e:
          print(e)

def delete_missao(self,id):
    try:
      
      db.session.query(Missao).filter(Missao.id==id).delete()
      db.session.commit()

    except Exception as e:
           print(e)

    

