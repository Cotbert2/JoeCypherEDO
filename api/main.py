from flask import Flask,request, jsonify
import cypher
app = Flask(__name__)

def joeCypher(data):

    if data['method'] == 'cypher':
        p = data['p']
        g = data['g']
        y = data['y']
        M = data['M']
        k = data['k']
        x = data['x']
        beta = data['beta']
        cypher_message = data['cypher_message']
        myCypher = cypher.Cypher(p, g, y, M, k, beta)
        print('ok')

        print(myCypher.encrypt())
        return myCypher.encrypt()
    elif data['method'] == 'decypher':
        p = data['p']
        g = data['g']
        y = data['y']
        M = data['M']
        k = data['k']
        x = data['x']
        beta = data['beta']
        cypher_message = data['cypher_message']
        myCypher = cypher.Cypher(p, g, y, M, k, beta)
        myCypher.decrypt(cypher_message, x)


@app.route('/', methods=['POST'])
def recibeJson():
    if request.method == 'POST':
        data = request.json

        return jsonify({'mensaje': 'Datos recibidos correctamente', 'Encriptacion': joeCypher(data)}), 200
    else:
        return jsonify({'error': 'Metodo no permitido'}), 405

if __name__ == '__main__':
    app.run()