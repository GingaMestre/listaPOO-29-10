from flask import Flask, request, jsonify

app = Flask(__name__)

id = 0
funcionario_db = []

@app.route('/funcionario', methods=['GET'])
def mostrarfuncionario():
    return jsonify(funcionario_db)

@app.route('/funcionario', methods=['POST'])
def adicionarfuncionario():
    global id
    id += 1
    dados= request.get_json()
    nome=dados.get('nome')
    cargo=dados.get('cargo')
    salario=dados.get('salario')
    funcionario = {"id": id, "nome": nome, "cargo": cargo, "salario": salario}
    funcionario_db.append(funcionario)
    return jsonify(funcionario)

@app.route('/funcionario/<int:id>', methods=['PUT'])
def atualizarfuncionario(id):
    dados = request.get_json()
    nome=dados.get('nome')
    cargo=dados.get('cargo')
    salario=dados.get('salario')
    for i in funcionario_db:
        if i['id'] == id:
            i['nome'] = nome
            i['cargo'] = cargo
            i['salario'] = salario
            return jsonify(i), 200
    return jsonify({"funcionario não encontrado"}), 404

@app.route('/funcionario/<int:id>', methods=['DELETE'])
def deletarfuncionario(id):
    for i in funcionario_db:
        if i['id'] == id:
            funcionario_db.remove(i)
        return "", 204
app.run(debug=True)
