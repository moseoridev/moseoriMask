from flask import Flask, render_template, request
import requests


def mask_info(lat, lng):
    url = 'https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByGeo/json'
    params = {'lat': lat, 'lng': lng, 'm': 3000}
    r = requests.get(url, params=params)
    return r.json()


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/show', methods=['POST'])
def show_stores():
    data = request.form
    lat = float(data['status'].split(',')[0])
    lng = float(data['status'].split(',')[1])
    i = mask_info(lat, lng)

    return render_template('show_stores.html', i=i)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
