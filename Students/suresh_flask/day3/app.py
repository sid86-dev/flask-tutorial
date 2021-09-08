from flask import Flask , render_template, request,redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['GET','POST'])
def process():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        age = request.form.get('age')
        gender = request.form.get('gender')
        return redirect(f'/profile/{name}/{email}/{number}/{age}/{gender}')
    return render_template('index.html')

@app.route('/profile/<string:name>/<string:email>/<int:number>/<int:age>/<string:gender>')
def profile(name,email,number,age,gender):
    return render_template('result.html',name=name,email=email,number=number,age=age,gender=gender)

if __name__ == '__main__':
    app.run(debug=True)