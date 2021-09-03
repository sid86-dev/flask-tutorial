from flask import Flask,request,render_template,redirect,session
app=Flask(__name__)
app.secret_key="Khushisecretkey"

#routes


@app.route("/register",methods=['GET','POST'])
def form():
    pass
@app.route("/login",methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        print(username)
        print(password)
        # this is a session variable
        session["user"]=username
        return render_template('result.html',username=username,password=password)
    return render_template('login.html')

@app.route("/")
def index():
    try:
        username=session["user"]
        if("user" in session and session["user"]==username):
            return render_template('result.html',username=username)
    except:
        return render_template('index.html')

@app.route("/forms",methods=['GET','POST'])
def forms():
    if request.method=='POST':
        name=request.form.get('name')
        phone=request.form.get('phone')
        email=request.form.get('email')
        age=request.form.get('age')
        stream=request.form.get('stream')
        address=request.form.get('address')
        print(name)
        print(phone)
        print(email)
        print(age)
        print(stream)
        print(address)
        return render_template('result.html',name=name, phone=phone,email=email,age=age,stream=stream,address=address)
    return render_template('login.html')

@app.route("/about")
def about():
        return render_template('about.html')

@app.route("/logout")
def logout():
    session.pop("user")
    return redirect("/")

@app.route("/test/<int:value>")
def test(value):
    print(type(value))
    return f"this is:{value}"

# this is sid's comment  

if __name__=="__main__":
    app.run(debug=True)