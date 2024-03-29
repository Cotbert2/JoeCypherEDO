from flask import Flask,request, jsonify
import cypher2
app = Flask(__name__)

def joeCypher(data):

    if data['method'] == 'cypher':
        M = data['M']
        cypherProcces = cypher2.JoeCypher()
        return cypherProcces.cypher(M)

    elif data['method'] == 'decypher':
        M = data['M']
        x = data['x']
        cypher_message = data['cypher_message']
        cypherProcces = cypher2.JoeCypher()
        return cypherProcces.decypher(x, cypher_message)


@app.route('/', methods=['POST'])
def recibeJson():
    if request.method == 'POST':
        data = request.json

        return jsonify({'mensaje': 'Datos recibidos correctamente', 'Encriptacion/texto_plano': joeCypher(data)}), 200
    else:
        return jsonify({'error': 'Metodo no permitido'}), 405

if __name__ == '__main__':
    app.run()