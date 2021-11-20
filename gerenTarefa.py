
from flask import Flask, request, jsonify
import json


app = Flask(__name__)

tarefas = [{
    'id': 0,
    'responsavel': 'Lucas',
    'tarefa': 'arrumar o quarto',
    'status': 'Nao concluido'},
    {
    'id': 1,
    'responsavel': 'Pedro',
    'tarefa': 'arrumar a sala',
    'status': 'Nao concluido'
}]


@app.route('/tarefa/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def lista_tarefas(id):
    if request.method == 'GET':
        try:
            response = tarefas[id]
        except:
            mensagem = ' O Id {} nao exixte' .format(id)
            response = {'status': 'erro', 'messagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        tarefas[id] = dados
        return jsonify(dados)

    elif request.method == 'DELETE':
        tarefas.pop(id)
        return ({'status': 'sucesso', 'mensagem': 'excluido com sucesso'})


@app.route('/tarefa', methods=['POST', 'GET'])
def tarefasLista():
    if request.method == 'POST':
        dadostarefa = json.loads(request.data)
        posicao = len(tarefas)
        dadostarefa['id'] = posicao
        tarefas.append(dadostarefa)
        return jsonify(tarefas[posicao])
    elif request.method == 'GET':
        return jsonify(tarefas)


if __name__ == '__main__':
    app.run(debug=True)
