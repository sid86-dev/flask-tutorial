from flask import Flask, render_template,redirect,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process',methods=['GET','POST'])
def process():
    if request.method=='POST':
        name = request.form.get("get_name")
        return redirect(f'/about/{name}')
    return "error"

@app.route('/about/<string:name>')
def about(name):
    return render_template('about.html',name=name)
    
if __name__=="__main__":
    app.run(debug=True)