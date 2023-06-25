#importing necessary libraries
from flask import Flask, jsonify, request
import requests
import argparse
import os

def openAI_request(prompt):
    # Refer api documentation of the openapi "https://platform.openai.com/docs/guides/gpt"
    api_endpoint = "https://api.openai.com/v1/completions"

    #add some value to environment variable
    # run the command ' $OPEN_API_KEY="key value"' in terminal
    #api_key = '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'
        
    api_key = str(os.environ["OPEN_API_KEY"])
    request_headers={ 
            "Content-Type": "application/json" ,
            "Authorization": "Bearer " + api_key }

    request_data={
        "model" : "text-davinci-003",
        "prompt" : prompt,
        "max_tokens" : 500,
        "temperature" : 0.5
    }
    response=requests.post(api_endpoint,headers=request_headers,json=request_data)

    if response.status_code == 200  :
        response_text=response.json()["choices"][0]["text"].strip()
        return response_text
    else:
        print(f"Request failed with status code {str(response.status_code)}")
        return f"Request failed with status code {str(response.status_code)}"

#creating Flask app
app = Flask(__name__)

#creating endpoint
@app.route('/api/symplr/<path_param>', methods=['GET'])
def get_data(path_param):
    #returning output
    return openAI_request(path_param).replace("\n","<br>")

#running the app
if __name__ == '__main__':
    app.run(host="192.168.1.6",debug=True)