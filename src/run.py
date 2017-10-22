from flask import Flask
from flask import render_template

import main
app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello():
	#main.q()
	return render_template('index.html')

@app.route('/my-link/')
def run():
	main.q()
	print("howdy")
	forward_message = "Moving Forward..."
	return render_template('index.html', message=forward_message)
