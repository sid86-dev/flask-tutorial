from flask import Flask,render_template,redirect,request

app=Flask(__name__)

@app.route('/', methods=['POST',"GET"])
def form():
    if request.method=='POST':
        name=request.form.get('name')
        age=request.form.get('age')
        cnum=request.form.get('cnum')
        date=request.form.get('date')
        email=request.form.get('email')
        password=request.form.get('password')
        address=request.form.get('address')
        gender=request.form.get('gender')
        city=request.form.get('city')
        
        return render_template('result.html',name=name,age=age,cnum=cnum,date=date,email=email,
        password=password,address=address,gender=gender,city=city)
    return render_template('form.html')

if __name__=="__main__":
    app.run(debug=True)