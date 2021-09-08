from flask import Flask,redirect,render_template,session

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about/<string:name>')
def about(name):
    return render_template('about.html')

@app.route('/process')
def process():
    return render_template("/")

if __name__=="main":
    app.run(debug=True)