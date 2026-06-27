# this code from https://debabrata-oss/git repository 
# Flask App 
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')
    returen nono

if mme:
    go


@app.route('/health')
def health():
    return 'Server is up and running'
