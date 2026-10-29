from flask import Flask, request, jsonify

app = Flask(__name__)

id = 0
filmes_db = []

@app.route('/filmes', methods=['GET'])
def mostrarFilmes():
    return jsonify(filmes_db)

@app.route('/filmes', methods=['POST'])
def adicionarFilme():
    global id
    id += 1
    dados= request.get_json()
    nome=dados.get('nome')
    ano=dados.get('ano')
    diretor=dados.get('diretor')
    filme = {"id": id, "nome": nome, "ano": ano, "diretor": diretor}
    filmes_db.append(filme)
    return jsonify(filme)

@app.route('/filmes/<int:id>', methods=['PUT'])
def atualizarFilme(id):
    dados = request.get_json()
    nome=dados.get('nome')
    ano=dados.get('ano')
    diretor=dados.get('diretor')
    for i in filmes_db:
        if i['id'] == id:
            i['nome'] = nome
            i['ano'] = ano
            i['diretor'] = diretor
            return jsonify(i), 200
    return jsonify({"Filme não encontrado"}), 404

@app.route('/filmes/<int:id>', methods=['DELETE'])
def deletarFilme(id):
    for i in filmes_db:
        if i['id'] == id:
            filmes_db.remove(i)
        return "", 204
app.run(debug=True)
