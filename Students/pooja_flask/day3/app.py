from flask import Flask,render_template 
from file_read_pooja import read_data 

 
app = Flask(__name__) 
 
 
@app.route("/") 
def index(): 
    data=read_data() 
    process_data = data.split("$") 
    length=len(process_data) 
    print(process_data) 
    print(length) 
    return render_template('index.html',process_data=process_data,length=length) 
 
 
if __name__=="__main__": 
     app.run(debug=True) 
