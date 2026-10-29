from flask import Flask, request, jsonify

app = Flask(__name__)

id = 0
cursos_db = []

@app.route('/cursos', methods=['GET'])
def mostrarcursos():
    return jsonify(cursos_db)

@app.route('/cursos', methods=['POST'])
def adicionarcursos():
    global id
    id += 1
    dados= request.get_json()
    nome=dados.get('nome')
    instituicao=dados.get('instituicao')
    duracao=dados.get('duracao')
    cursos = {"id": id, "nome": nome, "instituicao": instituicao, "duracao": duracao}
    cursos_db.append(cursos)
    return jsonify(cursos)

@app.route('/cursos/<int:id>', methods=['PUT'])
def atualizarcursos(id):
    dados = request.get_json()
    nome=dados.get('nome')
    instituicao=dados.get('instituicao')
    duracao=dados.get('duracao')
    for i in cursos_db:
        if i['id'] == id:
            i['nome'] = nome
            i['instituicao'] = instituicao
            i['duracao'] = duracao
            return jsonify(i), 200
    return jsonify({"cursos não encontrados"}), 404

@app.route('/cursos/<int:id>', methods=['DELETE'])
def deletarcursos(id):
    for i in cursos_db:
        if i['id'] == id:
            cursos_db.remove(i)
        return "", 204
app.run(debug=True)