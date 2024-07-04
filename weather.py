import requests
from flask import Flask, render_template, request, redirect, url_for, json
from toolbox.tools import parseJson

app = Flask(__name__)

apikey = "59983720c6894ce7ae5193852240107"
inputloc = "Los Angeles"

@app.route('/')
def  home():
    return render_template('index.html')

@app.route('/add', methods=['POST', 'GET'])
def add_city():
    if request.method == "POST":
        inputloc = request.form['content']
        response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={apikey}&q={inputloc}")
        data = response.json()
        try:
            parsed=parseJson(data)
        except KeyError as err:
            parsed = ["Sorry but the city name you entered is not valid, please try again. :)", f"KeyError: {err}"]
        return render_template('index.html', parsed=parsed )
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)