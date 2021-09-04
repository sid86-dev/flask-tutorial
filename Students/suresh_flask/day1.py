from flask import Flask

app = Flask(__name__)
@app.route("/<string:username>")
def index(username):
    name = f"Hello my name is {username}"
    return f"The output is = {name}"

if __name__ == "__main__":
    app.run(debug=True,port=8000)

