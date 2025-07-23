from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bholu-sound-api/predict', methods=['POST'])
def predict():
    audio = request.files['audio']
    # process audio
    return jsonify({'text': 'Transcribed text'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
