from flask import Flask, jsonify, request

from classifier import run

app = Flask(__name__)

@app.route('/issue_weighting', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        query = data['Title'] + ' ' + data['Body']
        stance = data['Stance']
    except Exception as e:
        return 'bad input or could not process.', 400

    return jsonify(run('oraw1_15k', query).tolist())

@app.route('/healthcheck')
def healthcheck():
    return 'ok', 200

print('ready')