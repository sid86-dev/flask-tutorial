from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('username')
        age = request.form.get('age')
        return redirect(f'/result/{name}/{age}')
        # return redirect('https://www.youtube.com/')
    return render_template('home.html')


@app.route('/result/<name>/<age>')
def result(name, age):
    return render_template('result.html', name=name, age=age)


app.run(debug=True)
