from flask import Flask, request, jsonify

app = Flask(__name__)

id = 0
musicas_db = []

@app.route('/musicas', methods=['GET'])
def mostrarmusicas():
    return jsonify(musicas_db)

@app.route('/musicas', methods=['POST'])
def adicionarMusica():
    global id
    id += 1
    dados= request.get_json()
    nome=dados.get('nome')
    ano=dados.get('ano')
    artista=dados.get('artista')
    musica = {"id": id, "nome": nome, "ano": ano, "artista": artista}
    musicas_db.append(musica)
    return jsonify(musica)

@app.route('/musicas/<int:id>', methods=['PUT'])
def atualizarmusica(id):
    dados = request.get_json()
    nome=dados.get('nome')
    ano=dados.get('ano')
    artista=dados.get('artista')
    for i in musicas_db:
        if i['id'] == id:
            i['nome'] = nome
            i['ano'] = ano
            i['artista'] = artista
            return jsonify(i), 200
    return jsonify({"musica não encontrada"}), 404

@app.route('/musicas/<int:id>', methods=['DELETE'])
def deletarmusica(id):
    for i in musicas_db:
        if i['id'] == id:
            musicas_db.remove(i)
        return "", 204
app.run(debug=True)