from flask import*

app = Flask(__name__)
app.secret_key = "pooja"  



@app.route('/login',methods=['GET','POST'])  
def login():  
    if request.method== 'POST':
       username=request.form.get('username')
       password=request.form.get('password')
       print(username)
       print(password)

       # this is a session variable
       session["user"]=username
       print('Value From Session ' + session["user"])
       
       return render_template('result.html',username=username,password=password)
    return render_template('login.html')            
            
             


    
@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/")
def home():
    try:
        username=session['user']
        if("user" in session and session["user"]==username):
           return render_template('result.html',username=username)
    except:
        return render_template('index.html')

@app.route("/logout")
def logout():
    session["user"] = None
    session.pop('user', None)
    return redirect("/")    
    
if __name__=="__main__":
    app.run(debug=True,port=8080)
