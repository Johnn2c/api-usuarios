from flask import Flask, request, json

app = Flask(__name__)

# para fins de teste, o "banco de dados" está em formato lista
usuarios = []
contador_id = 1


# Criar usuário
@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    global contador_id
    
    dados = request.get_json()

    usuario = {
        'id': contador_id,
        'nome': dados.get('nome'),
        'email': dados.get('email')
    }

    usuarios.append(usuario)
    contador_id += 1

    return json.dumps(usuario), 201

# Listar usuários
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return json.dumps(usuarios)

# Atualizar usuário
@app.route('/usuarios/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    dados = request.get_jason()

    for usuario in usuarios:
        if usuario['id'] == id:
            usuario['nome'] = dados.get('nome', usuario['nome'])
            usuario['email'] = dados.get('email', usuario['email'])
            return json.dumps(usuario)
    return json.dumps({'error': 'Usuário não encontrado'}), 404

# Deletar usuário
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def deletar_usuario(id):
    for usuario in usuarios:
        if usuario['id'] == id:
            usuarios.remove(usuario)
            return json.dumps({'message': 'Usuário deletado'})
    return json.dumps({'error': 'Usuário não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)