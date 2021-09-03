from flask import Flask,request,render_template,redirect

app=Flask(__name__)

#routes

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/register",methods=['GET','POST'])
def form():
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
        return render_template('result.html',username=name,phone=phone,email=email,age=age,stream=stream,address=address)
    return render_template('forms.html')



# this is sid's comment  

if __name__=="__main__":
    app.run(debug=True)