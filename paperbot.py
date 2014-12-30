from flask import Flask, render_template, url_for, redirect, request
import requests
from requests.auth import HTTPProxyAuth

app = Flask(__name__)

# configuration
DEBUG = True

@app.route('/')
def index():
    return render_template('layout.html')

@app.route('/search/', methods=['POST'])
def search():
 	url = request.form['url']
	r = requests.get(url)
	return r.text

@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('static', filename='page_not_found.html'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
