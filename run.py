from flask import Flask
from flask import render_template

#import main
app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello():
	#main.q()
	return render_template('index.html')
