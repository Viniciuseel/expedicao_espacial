from flask import jsonify
from flask_restful import Resource, reqparse
from app.models.missao import Mission


argumentos = reqparse.RequestParser()
argumentos.add_argument('id',type=int)
argumentos.add_argument('nome_missao',type=str)
argumentos.add_argument('data_lancamento',type=str)
argumentos.add_argument('data_final',type=int)
argumentos.add_argument('destino',type=str)
argumentos.add_argument('tripulacao',type=str)
argumentos.add_argument('carga_util',type=str)
argumentos.add_argument('duracao',type=int)
argumentos.add_argument('custo',type=float)
argumentos.add_argument('status',type=str)

argumentos_atualizar = reqparse.RequestParser()
argumentos_atualizar.add_argument('id',type=int)
argumentos_atualizar.add_argument('nome_missao',type=str)
argumentos_atualizar.add_argument('data_lancamento',type=str)
argumentos_atualizar.add_argument('data_final',type=int)
argumentos_atualizar.add_argument('destino',type=str)
argumentos_atualizar.add_argument('tripulacao',type=str)
argumentos_atualizar.add_argument('carga_util',type=str)
argumentos_atualizar.add_argument('duracao',type=int)
argumentos_atualizar.add_argument('custo',type=float)
argumentos_atualizar.add_argument('status',type=str)

argumentos_deletar = reqparse.RequestParser()
argumentos_deletar.add_argument('id',type=int)

class Index(Resource):
    def get(self):
        return jsonify("Welcome Aplication Flask")

class MissionCreate(Resource):
    def post(self):
        try:
            datas = argumentos.parse_args()
            Mission.criar_missao(self,
                                    datas['nome_missao'],
                                    datas['data_lancamento'], 
                                    datas['data_final'],
                                    datas['destino'], 
                                    datas['tripulacao'], 
                                    datas['carga_util'],
                                    datas['duracao'], 
                                    datas['custo'], 
                                    datas['status'])
            return {"message": 'Missao criada com sucesso!'}, 200
        except Exception as error:
            return jsonify({'status': 500, 'msg': f'{error}'}), 500

class MissionUpdate(Resource):
    def put(self):
        try:
            datas = argumentos_atualizar.parse_args()
            Mission.atualizar_missao(self, datas['id'], 
                                   datas['nome_missao'],
                                   datas['data_lancamento'],
                                   datas['data_final'],
                                   datas['destino'], 
                                   datas['tripulacao'],
                                   datas['carga_util'],
                                   datas['duracao'], 
                                   datas['custo'],
                                   datas['status'])
            return {"message": 'Mission update successfully!'}, 200    
        except Exception as error:
            return jsonify({'status': 500, 'msg': f'{error}'}), 500

class MissionDelete(Resource):
    def delete(self):
        try:
            datas = argumentos_deletar.parse_args()
            Mission.deletar_missao(self, datas['id'])
            return {"message": 'Missao deletada com sucesso!'}, 200    
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500
        
# class Index(Resource):
#     def get(self):
#         argumentos_get = reqparse.RequestParser()
#         argumentos_get.add_argument('id', type=int, required=True, help="O campo 'id' não pode ser deixado em branco.")

#         dados = argumentos_get.parse_args()
#         missao = Mission.buscar_missao(dados['id'])
#         if missao:
#             return missao.json(), 200
#         return {'message': 'Missão não encontrada.'}, 404
