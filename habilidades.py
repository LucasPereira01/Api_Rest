from flask_restful import Resource
from flask import request
import json

lista_Habilidades = [{'id': 0, 'Habilidade': 'Python'}, {'id': 1, 'Habilidade': 'Java'},

                     {'id': 2, 'Habilidade': 'PHP'}, {'id': 3, 'Habilidade': 'Node'}, {'id': 4, 'Habilidade': 'Rubi'}]


class Habilidades(Resource):
    def get(self):
        return lista_Habilidades

    def post(self):
        novaHabilidade = json.loads(request.data)
        if novaHabilidade in lista_Habilidades:
            return {'status': 'erro', 'messagem': 'habilidade ja existente'}
        else:
            lista_Habilidades.append(novaHabilidade)
            return {'status': 'sucesso', 'mensagem': 'Nova Habilidade Inserida'}


class Lista_Habilidade(Resource):
    def get(self, i):
        return lista_Habilidades[i]

    def put(self, i):
        dados = json.loads(request.data)
        posicao = len(lista_Habilidades)
        dados['id'] = posicao
        lista_Habilidades.append(dados)
        return lista_Habilidades[posicao]

    def delete(self, i):
        lista_Habilidades.pop(i)
        return {'status': 'sucessp', 'mensagem': 'Habilidade Exculida'}
