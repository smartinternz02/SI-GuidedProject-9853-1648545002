from flask import Flask, request, abort, jsonify
import json
import base64
import requests, io
import os
import pandas as pd
from ibm_watson_machine_learning import APIClient

app = Flask(__name__)

USERNAME = os.environ.get('raminedi.santhosh2020@vitstudent.ac.in')
PASSWORD = os.environ.get('Santhosh2002@')
URL = os.environ.get('https://recipe-recognition-app-excellent-possum-pa.eu-de.mybluemix.net')

WML_CREDENTIALS = {
                   "url": https://recipe-recognition-app-excellent-possum-pa.eu-de.mybluemix.net,
                   "username": "raminedi.santhosh2020@vitstudent.ac.in",
                   "password" : "Santhosh2002@",
                   "instance_id": "wml_local",
                   "version" : "3.5"
                  }

@app.route('/spaces/predictions', methods=['POST'])
def wml_scoring(space_id, deployment_id):
	if not request.json:
		abort(400)
	wml_credentials = WML_CREDENTIALS
	payload_scoring = {
        "input_data": [
            request.json
        ]
    }

	wml_client = APIClient(wml_credentials)
	wml_client.set.default_space(space_id)

	records_list=[]
	scoring_response = wml_client.deployments.score(deployment_id, payload_scoring)
	return jsonify(scoring_response["predictions"][0])

if __name__ == '__main__':
    app.run(host='https://recipe-recognition-app-excellent-possum-pa.eu-de.mybluemix.net', port=9443, debug=True)