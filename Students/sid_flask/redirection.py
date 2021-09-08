from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['GET', "POST"])
def process():
    if request.method == "POST":
        get_name = request.form.get("input_name")
        age = request.form.get("input_age")
        return redirect(f'/about/{get_name}/{age}')
    return "ERROR"

@app.route('/suresh')
def suresh():
    return render_template('suresh.html')


@app.route('/about/<string:apple>/<int:age>')
def about(apple, age):
    return render_template('about.html', get_name=apple, age=age)


if __name__ == "__main__":
    app.run(debug=True)
