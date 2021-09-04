from flask import Flask,render_template

app = Flask(__name__)

@app.route('/new')
def index():
    return render_template('index.html')

@app.route('/contact/<string:value>')
def method_name(value):
    return f"this is the string {value}"

@app.route('/int/<int:int>')
def about(int):
    return f"this is integer {int}"

@app.route('/table/<float:value>')
def new(value):
    return f"this is float value : {value}"




if __name__ == "__main__":
    app.run(debug=True,port=8000)
