#在整合式終端機執行用「flask --app index run」
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello,World!<p>"
