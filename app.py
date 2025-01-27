from flask import *

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/dimini/')
@app.route('/dimini')
def diminipage():
    return render_template('dimini.html')

@app.route('/quickstart/')
@app.route('/quickstart')
def quickstart():
    return render_template('quickstart.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='7272', debug = True)