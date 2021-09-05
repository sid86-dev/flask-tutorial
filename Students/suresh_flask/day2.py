from flask import Flask,render_template,redirect,request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == "POST":
        username = request.form.get('username','error')
        color = request.form.get('color','error')
        return render_template('result.html',username=username,color=color) 
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)