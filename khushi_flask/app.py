from flask import Flask,request,render_template,redirect

app=Flask(__name__)

#routes
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form.get('username')
        phone=request.form.get('phone')
        print(username)
        print(phone)
        return redirect('/')
    return render_template('login.html')

# this is sid's comment  

if __name__=="__main__":
    app.run(debug=True)