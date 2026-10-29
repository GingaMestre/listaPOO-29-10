from flask import Flask, request, jsonify
app = Flask(__name__)
id = 0
alunos_db = []

@app.route('/alunos', methods=['POST'])
def adicionarAlunos():
    global id
    id += 1
    dados= request.get_json()
    nome=dados.get('nome')
    curso=dados.get('curso')
    idade=dados.get('idade')
    aluno = {"id": id, "nome": nome, "curso": curso, "idade": idade}
    alunos_db.append(aluno)
    return jsonify(aluno)

@app.route('/alunos/<int:id>', methods=['PUT'])
def atualizarAluno(id):
    dados = request.get_json()
    nome=dados.get('nome')
    curso=dados.get('curso')
    idade=dados.get('idade')
    for i in alunos_db:
        if i['id'] == id:
            i['nome'] = nome
            i['curso'] = curso
            i['idade'] = idade
            return jsonify(i), 200
    return jsonify({"Aluno não encontrado"}), 404

@app.route('/alunos/<int:id>', methods=['DELETE'])
def deletarAluno(id):
    for i in alunos_db:
        if i['id'] == id:
            alunos_db.remove(i)
        return "", 204

@app.route('/alunos', methods=['GET'])
def mostrarFilmes():
    return jsonify(alunos_db)
app.run(debug=True)