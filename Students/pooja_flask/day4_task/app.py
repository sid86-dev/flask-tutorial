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
        gender = request.form.get("input_gender")
        food =  request.form.get("input_food")
        return redirect(f'/about/{get_name}/{age}/{gender}/{food}')
    return "ERROR"



@app.route('/about/<string:apple>/<int:age>/<string:gender>/<string:food>')
def about(apple, age,gender,food):
    return render_template('about.html', get_name=apple, age=age, gender=gender,food = food)


if __name__ == "__main__":
    app.run(debug=True)