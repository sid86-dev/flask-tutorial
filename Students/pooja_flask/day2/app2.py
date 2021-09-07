from flask import Flask, render_template, request, redirect

app= Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == "POST":
        username = request.form.get('username','')
        color= request.form.get('color')
        return render_template("result2.html", username=username ,color=color)
    return render_template('index2.html')


if __name__=='__main__':
    app.run(debug=True)