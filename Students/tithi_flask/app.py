from flask import Flask

app = Flask(__name__)

#this is home end point
@app.route("/")
def hello_world():
    return "Hello, World! my name is tithi"
# this is login end point
@app.route("/login")
def login():
    return "this is login page"
# this is contact end point
@app.route("/contact")
def contact():
    return "this is contact page"
#test endpoint
@app.route("/test/<path:value>")
def test(value):
    print(type(value))
    return f"hi this is path {value}"

if __name__=="__main__":
    app.run(debug=True,port=8000)

