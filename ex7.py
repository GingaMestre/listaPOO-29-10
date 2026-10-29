from flask import Flask, request, jsonify

app = Flask(__name__)

id = 0
cidades_db = []

@app.route('/cidades', methods=['GET'])
def mostrarcidades():
    return jsonify(cidades_db)

@app.route('/cidades', methods=['POST'])
def adicionarcidades():
    global id
    id += 1
    dados= request.get_json()
    nome=dados.get('nome')
    preco=dados.get('preco')
    categoria=dados.get('categoria')
    cidades = {"id": id, "nome": nome, "preco": preco, "categoria": categoria}
    cidades_db.append(cidades)
    return jsonify(cidades)

@app.route('/cidades/<int:id>', methods=['PUT'])
def atualizarcidades(id):
    dados = request.get_json()
    nome=dados.get('nome')
    preco=dados.get('preco')
    categoria=dados.get('categoria')
    for i in cidades_db:
        if i['id'] == id:
            i['nome'] = nome
            i['preco'] = preco
            i['categoria'] = categoria
            return jsonify(i), 200
    return jsonify({"cidades não encontrados"}), 404

@app.route('/cidades/<int:id>', methods=['DELETE'])
def deletarcidades(id):
    for i in cidades_db:
        if i['id'] == id:
            cidades_db.remove(i)
        return "", 204
app.run(debug=True)
