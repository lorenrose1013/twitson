from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/personality')
def personality():
    if request.method == "GET":
        handle = request.args.get('handle')
    return render_template("personality.html", user=handle)

if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0', port=8000)
