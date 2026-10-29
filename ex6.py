from flask import Flask, request, jsonify

app = Flask(__name__)

id = 0
carros_db = []

@app.route('/carros', methods=['GET'])
def mostrarcarros():
    return jsonify(carros_db)

@app.route('/carros', methods=['POST'])
def adicionarcarros():
    global id
    id += 1
    dados= request.get_json()
    modelo=dados.get('modelo')
    marca=dados.get('marca')
    ano=dados.get('ano')
    carros = {"id": id, "modelo": modelo, "marca": marca, "ano": ano}
    carros_db.append(carros)
    return jsonify(carros)

@app.route('/carros/<int:id>', methods=['PUT'])
def atualizarcarros(id):
    dados = request.get_json()
    modelo=dados.get('modelo')
    marca=dados.get('marca')
    ano=dados.get('ano')
    for i in carros_db:
        if i['id'] == id:
            i['modelo'] = modelo
            i['marca'] = marca
            i['ano'] = ano
            return jsonify(i), 200
    return jsonify({"carros não encontrados"}), 404

@app.route('/carros/<int:id>', methods=['DELETE'])
def deletarcarros(id):
    for i in carros_db:
        if i['id'] == id:
            carros_db.remove(i)
        return "", 204
app.run(debug=True)
