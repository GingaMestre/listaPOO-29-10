from flask import Flask, request, jsonify

app = Flask(__name__)

id = 0
restaurantes_db = []

@app.route('/restaurantes', methods=['GET'])
def mostrarrestaurantes():
    return jsonify(restaurantes_db)

@app.route('/restaurantes', methods=['POST'])
def adicionarrestaurantes():
    global id
    id += 1
    dados= request.get_json()
    nome=dados.get('nome')
    tipo=dados.get('tipo')
    cidade=dados.get('cidade')
    restaurantes = {"id": id, "nome": nome, "tipo": tipo, "cidade": cidade}
    restaurantes_db.append(restaurantes)
    return jsonify(restaurantes)

@app.route('/restaurantes/<int:id>', methods=['PUT'])
def atualizarrestaurantes(id):
    dados = request.get_json()
    nome=dados.get('nome')
    tipo=dados.get('tipo')
    cidade=dados.get('cidade')
    for i in restaurantes_db:
        if i['id'] == id:
            i['nome'] = nome
            i['tipo'] = tipo
            i['cidade'] = cidade
            return jsonify(i), 200
    return jsonify({"restaurantes não encontrados"}), 404

@app.route('/restaurantes/<int:id>', methods=['DELETE'])
def deletarrestaurantes(id):
    for i in restaurantes_db:
        if i['id'] == id:
            restaurantes_db.remove(i)
        return "", 204
app.run(debug=True)
