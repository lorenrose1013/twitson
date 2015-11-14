from flask import Flask, render_template, request
import utils

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/personality')
def personality():
	if request.method == "GET" and request.args.get('handle') != '':
		handle = request.args.get('handle')
	else:
		handle = utils.getRandomHandle()
	personalityDict = utils.getPersonalityDict(handle)
	if personalityDict == None:
		return "no"
	return render_template("personality.html", user='@'+handle, personalityDict=personalityDict)

if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0', port=8000)
