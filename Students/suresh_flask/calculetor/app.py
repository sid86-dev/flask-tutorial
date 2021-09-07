from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        number1 = float(request.form.get('number1'))
        number2 = float(request.form.get('number2'))
        option = request.form.get('option', "add")
        if option == "add":
            total = number1 + number2
        elif option == "sub":
            total = number1 - number2
        elif option == "multi":
            total = number1 * number2
        elif option == "div":
            total = number1 / number2
        return render_template('result.html', total=total)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)