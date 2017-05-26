#! /usr/bin/env python
import os
from flask import Flask, jsonify, request
from voice_synthesizer import VoiceSynthesizer

aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_key_id = os.getenv('AWS_SECRET_KEY_ID')
aws_region_name = os.getenv('AWS_REGION_NAME')

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
    app.run(debug=True)