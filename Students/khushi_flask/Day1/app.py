from flask import Flask,render_template
from file_read import read_data

#create a flask template
app=Flask(__name__)

@app.route('/')
def index():
    data=read_data()
    #getting list by procesing the data
    process_data=data.split("$")
    length1=len(process_data)
    return render_template('index.html',process_data=process_data,length1=length1)

if __name__=="__main__":
    app.run(debug=True)