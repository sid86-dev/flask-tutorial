from flask import Flask,render_template,redirect,request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='POST':
        name=request.form.get('name','error')
        colour=request.form.get('colour','error')
        return render_template('result.html',name=name,colour=colour)
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
