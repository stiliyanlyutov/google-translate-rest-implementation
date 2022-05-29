from flask import Flask, request
import requests
import codecs
import json

app = Flask(__name__) #creates server
 
@app.route("/")
def index(): 
    return "Hello"

@app.route("/translate")  
def translate():
    text = request.args.get("text")
    
    dest = request.args.get("dest")

    src = request.args.get("src")



    url = "https://translo.p.rapidapi.com/api/v3/translate"

    payload = "from=" + src + "&to=" + dest + "&text=" + text
    payload = codecs.encode(payload, "utf-8")
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Host": "translo.p.rapidapi.com",
        "X-RapidAPI-Key": "" 
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    k = json.loads(response.text)
    return k["translated_text"]


if __name__ == '__main__':
    app.run(debug = True) #runs the server
