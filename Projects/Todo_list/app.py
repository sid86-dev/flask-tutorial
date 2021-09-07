from flask import Flask, render_template
from file_read import read_data

app = Flask(__name__)

@app.route("/")
def index():   
    # get data as a string
    data = read_data()
    # getting a list by processing the data
    process_data = data.split("$")
    # passing the list to the index file
    length  = len(process_data)
  
    return render_template('index.html', process_data=process_data, length=length)

if __name__=="__main__":
    app.run(debug=True)