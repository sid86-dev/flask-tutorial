from flask import Flask

app = Flask(__name__)

#This is home endpoint
@app.route('/')

def home():
    return "Hello World Abinash"

#This is login endpoint
@app.route('/login')
def login():
    return "This is Login page."

#This is contact endpoint
@app.route('/contact')
def contact():
    return "This is Contact page."

#This is test endpoint
@app.route("/test/<string:value>")
def test(value):
    return f"This is Test page{value}"


if(__name__) == "__main__":
    app.run(debug=True, port=8000)