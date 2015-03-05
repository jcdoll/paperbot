from flask import Flask, flash, render_template, url_for, redirect, request
from requests.auth import HTTPProxyAuth
import requests, re, mechanize, os, cookielib, random, time

cookies_filename = 'cookies.txt'
pdf_filename = 'fetched_paper.pdf'

app = Flask(__name__)
app.debug = True
app.config.from_object('config')
app.secret_key = 'secrets_are_fun'

@app.route('/')
def index():
    return render_template('layout.html')

@app.route('/search/', methods=['POST'])
def search():
 	url = request.form['url']
	proxies = {'http': app.config['PROXY_SERVER']}

	# setup mechanize browser
	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.set_proxies(proxies)
	cj = cookielib.LWPCookieJar()
	br.set_cookiejar(cj)
	if os.path.isfile(cookies_filename):
		cj.load(cookies_filename, ignore_discard=False, ignore_expires=False)

	# Try to navigate to paper url
	response = br.open(url)

	# Login if required
	if br.title() == 'Stanford WebLogin' and any(map(lambda form: form.name == 'login', br.forms())):
		br.select_form(name="login")
		br.form['username'] = app.config['USERNAME']
		br.form['password'] = app.config['PASSWORD']
		response = br.submit()
		result = response.read()
	else:
		flash('foo')
		return render_template('layout.html')

	# Enter OTP if required and save updated cookie to avoid OTP for a month
	if br.title() == 'Stanford WebLogin' and any(map(lambda form: form.name == 'login', br.forms())):
		br.select_form(name="login")
		br.form['otp'] = app.config['OTP']
		response = br.submit()
		result = response.read()

		# After two-factor, save our updated cookies
		cj.save(cookies_filename, ignore_discard=False, ignore_expires=False)

	# Find the PDF link
	# TODO: Generalize detection
	pdf_url = ''
	for link in br.links(text_regex='(.*)(?i)pdf(.*)'):
		response = br.follow_link(link)
		result = response.read()

		# Find any pdf urls
		search_result = re.search(r'"http://(.*)pdf(.*)"', result, re.MULTILINE)
		if search_result is not None:
			pdf_url = search_result.group(0)[1:-1]
			break
		else: # try again
			br.back()

	if not pdf_url:
		flash('No pdf found')
		return redirect(url_for('index'))

	# Download the pdf and then provide to user
	br.retrieve(pdf_url, './static/' + pdf_filename)
	return redirect(url_for('static', filename=pdf_filename))

@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('static', filename='page_not_found.html'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
