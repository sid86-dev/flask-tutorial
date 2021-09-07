from flask import Flask, render_template , redirect , request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods = ['GET','POST'])
def process():
    if request.method == "POST":
        get_name = request.form.get("input_name")
        return redirect(f'about/{get_name}')
    return "Error"

@app.route('/about/<string:get_name>')
def about(get_name):
    return render_template('about.html',get_name=get_name)

if __name__ == '__main__':
    app.run(debug=True)