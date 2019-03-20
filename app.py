from flask import Flask
from flask import render_template
from flask import request
import json
import requests

app = Flask(__name__)
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    url = 'https://api.github.com'
    payload = {'some': 'data'}
    headers = {
	'Authorization':'2c8795d187b5265c3744dcad0b2261562ea58be5'
	}
 
    r = requests.get(url, data=json.dumps(payload), headers=headers)
    print(r)
    return render_template('hello.html', name=r.json())
