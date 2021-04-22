from flask import Flask, render_template
import requests
import json
import secrets as secrets

client_key = secrets.api_key
client_secret = secrets.api_secret

app = Flask(__name__)    

@app.route('/')
def index():     
    return '<h1>Welcome!</h1>'

@app.route('/name/<nm>')
def hello_name(nm):
    return render_template('name.html', name=nm) 

@app.route('/headlines/<nm>')
def top(nm):
    base = "https://api.nytimes.com/svc/topstories/v2/"
    url = f"{base}technology.json?api-key={client_key}"
    result = requests.get(url).json()
    top_5 = []
    i=1
    for item in result["results"]:
        if i<=5:
            name = item["title"]
            top_5.append(name)
            i+=1
    return render_template('headlines.html', name=nm, items=top_5) 

if __name__ == '__main__':
    print('starting Flask app', app.name)  
    app.run(debug=True)
    