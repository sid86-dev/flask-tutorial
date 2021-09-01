from flask import*

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login',methods=['GET','POST'])  
def login():  
    if request.method== 'POST':
       username=request.form.get('username')
       email=request.form.get('email')
       print(username)
       print(email)
       return render_template('result.html',username=username,email=email)
    return render_template('login.html')

if __name__=="__main__":
    app.run(debug=True,port=8080)


   