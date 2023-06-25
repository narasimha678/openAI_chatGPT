import requests
import argparse
import os

# Reference Video https://www.youtube.com/watch?v=w-X_EQ2Xva4

parser = argparse.ArgumentParser()
parser.add_argument("prompt",help="The prompt to send to the openAI API")
parser.add_argument("file_name",help="Name of the file to save the output")
args = parser.parse_args()

# Refer api documentation of the openapi "https://platform.openai.com/docs/guides/gpt"
#new api end point
#api_endpoint = "https://api.openai.com/v1/chat/completions"

#old api end point
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
    "prompt" : args.prompt,
    "max_tokens" : 4000,
    "temperature" : 0.5
}
response=requests.post(api_endpoint,headers=request_headers,json=request_data)

if response.status_code == 200  :
   response_text=response.json()["choices"][0]["text"].strip()
   with open(args.file_name,"w") as file :
       file.write(response_text)
       
else:
    print(f"Request failed with status code {str(response.status_code)} and response as {str(response.json())}")
