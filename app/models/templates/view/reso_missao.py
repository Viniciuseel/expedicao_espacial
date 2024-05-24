from flask import jsonify
from flask_restful import Resource, reqparse 
from app.models.missao import Missao

argumentos = reqparse.RequestParse()
argumentos.add_argument('name',type=str)
argumentos.add_argument('data', type=int)

argumentos_update = reqparse.RequestParse()
argumentos_update.add_argument('id', type=int)
argumentos_update.add_argument('nome', type=str)
argumentos_update.add_argument('data', type=int)

argumentos_delete = reqparse.RequestParse()
argumentos_delete.add_argument('id', type=int)

class Index(Resource):
    def get(self):
        return jsonify("Olá Mundo")

class MissaoCreate(Resource):
    def post(self):        
            try:
                datas = argumentos.parse_args()
                Missao.save_missao(self, datas['id'], datas['nome'], datas ['datas'])
                return {"message": 'Missão criada com sucesso'}, 200
            
            except Exception as e:
                return jsonify({'status':500, 'msg':f'{e}'}), 500
            
class MissaoUpdate(Resource):
     def put(self):
          try:
                datas = argumentos_update.parse_args()
                Missao.update_missao(self, datas['id'], datas['nome'], datas ['datas'])
                return {"message": 'Missão Atualizada com sucesso'}, 200
          except Exception as e:
                return jsonify({'status':500, 'msg':f'{e}'}), 500
          
class MissaoDelete(Resource):
     def delete(self):
          try:
                datas = argumentos_delete.parse_args()
                Missao.delete_missao(self, datas['id'])
                return {"message": 'Missão Excluída com sucesso'}, 200
          except Exception as e:
                return jsonify({'status':500, 'msg':f'{e}'}), 500
          
          
               
        
    
    

