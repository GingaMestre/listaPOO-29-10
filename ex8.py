from flask import Flask, request, jsonify

app = Flask(__name__)

id = 0
jogos_db = []

@app.route('/jogos', methods=['GET'])
def mostrarjogos():
    return jsonify(jogos_db)

@app.route('/jogos', methods=['POST'])
def adicionarjogos():
    global id
    id += 1
    dados= request.get_json()
    nome=dados.get('nome')
    genero=dados.get('genero')
    ano=dados.get('ano')
    jogos = {"id": id, "nome": nome, "genero": genero, "ano": ano}
    jogos_db.append(jogos)
    return jsonify(jogos)

@app.route('/jogos/<int:id>', methods=['PUT'])
def atualizarjogos(id):
    dados = request.get_json()
    nome=dados.get('nome')
    genero=dados.get('genero')
    ano=dados.get('ano')
    for i in jogos_db:
        if i['id'] == id:
            i['nome'] = nome
            i['genero'] = genero
            i['ano'] = ano
            return jsonify(i), 200
    return jsonify({"jogos não encontrados"}), 404

@app.route('/jogos/<int:id>', methods=['DELETE'])
def deletarjogos(id):
    for i in jogos_db:
        if i['id'] == id:
            jogos_db.remove(i)
        return "", 204
app.run(debug=True)
