from flask import Flask, request, jsonify

app = Flask(__name__)

id = 0
produtos_db = []

@app.route('/produtos', methods=['GET'])
def mostrarprodutos():
    return jsonify(produtos_db)

@app.route('/produtos', methods=['POST'])
def adicionarprodutos():
    global id
    id += 1
    dados= request.get_json()
    nome=dados.get('nome')
    preco=dados.get('preco')
    categoria=dados.get('categoria')
    produtos = {"id": id, "nome": nome, "preco": preco, "categoria": categoria}
    produtos_db.append(produtos)
    return jsonify(produtos)

@app.route('/produtos/<int:id>', methods=['PUT'])
def atualizarprodutos(id):
    dados = request.get_json()
    nome=dados.get('nome')
    preco=dados.get('preco')
    categoria=dados.get('categoria')
    for i in produtos_db:
        if i['id'] == id:
            i['nome'] = nome
            i['preco'] = preco
            i['categoria'] = categoria
            return jsonify(i), 200
    return jsonify({"produtos não encontrados"}), 404

@app.route('/produtos/<int:id>', methods=['DELETE'])
def deletarprodutos(id):
    for i in produtos_db:
        if i['id'] == id:
            produtos_db.remove(i)
        return "", 204
app.run(debug=True)
