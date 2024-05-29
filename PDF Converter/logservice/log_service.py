from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def log():
    data = request.get_json()
    token = request.headers.get('Authorization')
    if token == "token-david-kaue-moises-vitor":
        with open("/logs/logs.txt", "a") as log_file:
            log_file.write(f"{datetime.datetime.now()}: {data}\n")
        return jsonify({"message": "Log registrado"}), 200
    else:
        return jsonify({"message": "Não autorizado"}), 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8083)
