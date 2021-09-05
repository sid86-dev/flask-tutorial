from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])

def home():
    if request.method == "POST":
        name = request.form.get('name','error')
        email = request.form.get('emial')
        password = request.form.get('password')
        number = request.form.get('number')
        return render_template('day3result2.html',name=name,email=email,password=password,number=number)
    return render_template('result2.html')

if __name__ == '__main__':
    app.run(debug = True)