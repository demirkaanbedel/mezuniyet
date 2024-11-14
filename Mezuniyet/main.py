from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/videolar')
def videolar():
    return render_template("videolar.html")

@app.route('/hakkımda')
def hakkımda():
    return render_template("hakkımda.html")   
app.run(debug=True)