from flask import Flask, request, jsonify, make_response
from tabela_de_token import main
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/analyze": {"origins": "http://localhost:3000"}})

@app.route('/analyze', methods=['POST'])
def analyze_code():
    data = request.get_json()
    code = data.get('code')

    # Chame a função main() do seu código Python com o código do cliente
    result = main(code)

    # Responder com a resposta da análise
    response_data = {
        'message': result
    }
    return jsonify(response_data)

if __name__ == '__main__':
    app.run()
