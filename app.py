import os
from flask import Flask, jsonify, request
from voice_synthesizer import VoiceSynthesizer

aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID') #AKIAINIGFWBBXXHOP3SA
aws_secret_key_id = os.getenv('AWS_SECRET_KEY_ID') #Dxfgs0j8g6RV5hKabsW+Q3tyIJS3/pkj11irwhk5
aws_region_name = os.getenv('AWS_REGION_NAME') # us-west-2

vs = VoiceSynthesizer(
    volume=1, 
    region_name=aws_region_name, 
    aws_access_key_id=aws_access_key_id, 
    aws_secret_access_key=aws_secret_key_id)

app = Flask(__name__)

@app.route('/', methods=['POST'])
def say():
    if not request.json or not 'text' in request.json:
        return jsonify({'error': 'Missing text'}), 400

    voice = vs.synthesize('text')
    return jsonify({'sound': voice});

if __name__ == "__main__":
    app.run()