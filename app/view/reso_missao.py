from datetime import datetime
from flask import jsonify, make_response, request
from flask_restful import Resource, reqparse
from app.models.missao import Mission

# Argumentos para criação
argumentos = reqparse.RequestParser()
argumentos.add_argument('nome_missao', type=str, required=True)
argumentos.add_argument('data_lancamento', type=str, required=True)
argumentos.add_argument('destino', type=str, required=True)
argumentos.add_argument('tripulacao', type=str, required=True)
argumentos.add_argument('carga_util', type=str, required=True)
argumentos.add_argument('duracao', type=str, required=True)
argumentos.add_argument('custo', type=float, required=True)
argumentos.add_argument('status', type=str, required=True)
argumentos.add_argument('status_detalhado', type=str, required=True)

# Argumentos para criação
argumentos_update = reqparse.RequestParser()
argumentos_update.add_argument('id', type=int, required=True)
argumentos_update.add_argument('nome_missao', type=str, required=True)
argumentos_update.add_argument('data_lancamento', type=str, required=True)
argumentos_update.add_argument('destino', type=str, required=True)
argumentos_update.add_argument('tripulacao', type=str, required=True)
argumentos_update.add_argument('carga_util', type=str, required=True)
argumentos_update.add_argument('duracao', type=str, required=True)
argumentos_update.add_argument('custo', type=float, required=True)
argumentos_update.add_argument('status', type=str, required=True)
argumentos_update.add_argument('status_detalhado', type=str, required=True)

# Argumentos para deleção
argumentos_deletar = reqparse.RequestParser()
argumentos_deletar.add_argument('id', type=int, required=True)

class MissionsListView(Resource):
    def get(self):
        try:
            missoes = []
            serialized_missions = []

            if request.args.get("dataInicial") is None or request.args.get("dataFinal") is None:
                missoes = Mission.listarMissao(self)
            else:
                dataInicial = datetime.strptime(request.args.get("dataInicial"), "%d-%m-%Y")
                dataFinal = datetime.strptime(request.args.get("dataFinal"), "%d-%m-%Y")
                missoes = Mission.listarPorData(self, dataInicial, dataFinal) or []
            
            for missao in missoes:
                serialized_mission = {
                    "id": missao.id,
                    "nome_missao": missao.nome_missao,
                    "data_lancamento": missao.data_lancamento.strftime("%d/%m/%Y"), 
                    "duracao": missao.duracao.strftime("%d/%m/%Y %H:%M"), 
                    "destino": missao.destino,
                    "status": missao.status
                }
                serialized_missions.append(serialized_mission)

            return make_response(jsonify({"missoes": serialized_missions}), 200)
        except Exception as e:
            print("Ocorreu um erro na listagem")
            print(e)
            return make_response(jsonify({"msg": "Internal Error"}), 500)
        
    def post(self):
        try:
            data = argumentos.parse_args()
            data_lancamento = datetime.strptime(data["data_lancamento"], "%d/%m/%Y")
            duracao = datetime.strptime(data["duracao"], "%d/%m/%Y %H:%M")

            if data_lancamento > duracao:
                return make_response(jsonify({"msg": "A data de lançamento deve ser anterior à duração"}), 400)

            Mission.criarMissao(self, data['nome_missao'],
                                data_lancamento,
                                data['destino'], 
                                data['tripulacao'],
                                data['carga_util'],
                                duracao, 
                                data['custo'],
                                data['status'],
                                data['status_detalhado'])

            return make_response(jsonify({"msg": "Missão criada com sucesso!"}), 201)
        except Exception as e:
            print("Ocorreu um erro")
            print(e)
            return make_response(jsonify({"msg": "Internal Error"}), 500)
        
    def put(self):
            try:
                data = argumentos_update.parse_args()
                data_lancamento = datetime.strptime(data["data_lancamento"], "%d/%m/%Y")
                duracao = datetime.strptime(data["duracao"], "%d/%m/%Y %H:%M")

                if data_lancamento > duracao:
                    return make_response(jsonify({"msg": "A data de lançamento deve ser anterior à duração"}), 400)

                data["data_lancamento"] = data_lancamento
                data["duracao"] = duracao

                Mission.atualizarMissao(self, data["id"], data)
                return make_response(jsonify({"msg": "Missão atualizada com sucesso"}), 200)
            except Exception as e:
                print("Ocorreu um erro ao atualizar a missão")
                print(e)
                return make_response(jsonify({"msg": "Internal Error"}), 500)

    def delete(self):
        try:
            data = argumentos_deletar.parse_args()
            if (data["id"] is None) :
                return make_response(jsonify({"msg": "Id não pode ser vazio"}), 400)

            Mission.deletarMissao(self, data["id"]) 
            return make_response(jsonify({"msg": "Missão deletada com sucesso!"}), 200)
        except Exception as e:
            print("Ocorreu um erro ao deletar a missão")
            print(e)
            return make_response(jsonify({"msg": "Internal Error"}), 500)


class MissionsView(Resource):
    def get(self, id):
        try:
            missao = Mission.buscarMissao(self, id)
            if missao is None:
                return make_response(jsonify(), 404)
            
            serialized_mission = {
                "id": missao.id,
                "nome_missao": missao.nome_missao,
                "data_lancamento": missao.data_lancamento.strftime("%d/%m/%Y"),
                "destino": missao.destino,
                "tripulacao": missao.tripulacao,
                "carga_util": missao.carga_util,
                "duracao": missao.duracao.strftime("%d/%m/%Y %H:%M"),
                "custo": float(missao.custo),
                "status": missao.status
            }
            return make_response(jsonify({"missao": serialized_mission}), 200)
        except Exception as e:
            print(e)
            return make_response(jsonify({"msg": "Internal Error"}), 500)
