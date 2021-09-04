from flask import Flask,request,render_template,redirect,session
app=Flask(__name__)
app.secret_key="flasksecretkey"

@app.route("/<string:username>")
def index(username):
    name=f"Hello I am {username}"
    return f"output is {name}"

@app.route("/test/<int:value>")
def test(value):
    print(type(value))
    return f"this is:{value}"

@app.route("/test1/<string:value>")
def test1(value):
    print(type(value))
    return f"this is:{value}"

@app.route("/test2/<float:value>")
def test2(value):
    print(type(value))
    return f"this is:{value}"

@app.route("/test3/<path:value>")
def test3(value):
    print(type(value))
    return f"this is:{value}"

if __name__=="__main__":
    app.run(debug=True,port=4000)