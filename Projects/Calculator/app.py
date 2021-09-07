from logging import debug
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/', methods=['GET',"POST"])
def home():
    if request.method == "POST":
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        add = int(num1) + int(num2)
        return render_template('result.html', add=add)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)