from flask import Flask,render_template,redirect,request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='POST':
        fnum=int(request.form.get('fnum'))
        snum=int(request.form.get('snum'))
        calculator=request.form.get('calculator')
        result=request.form.get('result')
        if calculator=='Addition':
            result=fnum+snum
        if calculator=='Subtraction':
            result=fnum-snum
        if calculator=='Multiplication':
            result=fnum*snum
        if calculator=='Division':
            result=fnum/snum
        return render_template('result.html',result=result)
    return render_template('calculater.html')

if __name__=="__main__":
    app.run(debug=True)
