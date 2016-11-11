import requests
import datetime as dt
from flask import Flask, render_template, request


app = Flask(__name__)
BASE_API_URL = 'http://127.0.0.1:1212/'
USER_API_URL = BASE_API_URL + 'users/'
CLIENT_API_URL = BASE_API_URL + 'clients/'
PRODUCTS_API_URL = BASE_API_URL + 'products/'
REQUESTS_API_URL = BASE_API_URL + 'requests/'


@app.route('/')
def index():
    name = requests.get(USER_API_URL).json()['_items'][0]['username']
    current = requests.get(REQUESTS_API_URL).json()['_items']
    return render_template('base.html', name=name, current=current)


@app.route('/style')
def style():
    return render_template('test.html')


@app.route('/request', methods=['GET', 'POST'])
def new_request():
    """ I'm in charge of submitting pretty new feature requests.
        There is most definitely a better way to do this out there.
    """

    if request.method == 'POST':
        # grab item ID's since that is what our API is looking for
        client, product_areas = request.form['client'], request.form['product_areas']
        client_id = requests.get(CLIENT_API_URL + client).json()['_id']
        product_areas_id = requests.get(PRODUCTS_API_URL + product_areas).json()['_id']

        # our API wants datetime objects, so we need to do a bit of formatting
        y, m, d = (int(i) for i in request.form['target_date'].split('-'))
        today = dt.datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT")
        target = dt.datetime(y,m,d).strftime("%a, %d %b %Y %H:%M:%S GMT")

        payload = {
            'client': client_id,
            'product_areas': product_areas_id,
            'open_date': today,
            'target_date': target,
            'title': request.form['title'],
            'description': request.form['description'],
            'priority': int(request.form['priority']),
            'request_url': request.form['request_url']
        }
        headers = {
            'cache-control': "no-cache",
            'content-type': "application/x-www-form-urlencoded"
        }
        response = requests.request("POST", REQUESTS_API_URL, data=payload, headers=headers)

        error = response.text
        return error

    return render_template('request.html')


if __name__ == '__main__':
    app.run(debug=True, port=2222)
