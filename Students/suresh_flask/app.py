from flask import Flask

app = Flask(__name__)
@app.route("/")

def index():
    return "hello world bvjhbkjnmhjbm"

# this is log in page

@app.route("/login")
def login():
    return "hjmgmmghmg"

# this is home page 

@app.route('/home')
def home():
    return "chgggnf home"

# contact page 

@app.route('/contact')
def contact():
    return " contact page"

# test 

@app.route('/test/<float:value>')
def test(value):
    print(type(value))
    return f"this is inter {value}" 

if __name__ == "__main__":
    app.run(debug=True,port=8000)

