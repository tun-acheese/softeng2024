from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello():
    return 'Hello world!'

@app.route("/hello/<name>")
def say_hello(name):
    return f"안녕하세요1.{escape(name)}님."

@app.route("/dan/<dan>")
def gugudan_html(dan):
    html_str = ""
    for i in range(1,10):
        html_str += f"{dan} X {i} = {int(dan)*i}<br>"
    return html_str

@app.route("/gugudan/")
def gugudan_html_dan():
    dan = request.args.get("dan")
    html_str = ""
    for i in range(1, 10):
        html_str += f"{dan} X {i} = {int(dan) * i}<br>"
    return html_str

    html_str = ""


app.run(debug=True)
