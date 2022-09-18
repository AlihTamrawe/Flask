from operator import index
from time import time
from flask import Flask, render_template 

#----------------------------1-halloworld

app = Flask(__name__)    

@app.route('/')
def render_list():
    return render_template("index.html")

@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
       {'name' : 'Michael', 'age' : 35},
       {'name' : 'John', 'age' : 30 },
       {'name' : 'Mark', 'age' : 25},
       {'name' : 'KB', 'age' : 27}
    ]
    return render_template("index.html", student = student_info, length = len(student_info))

if __name__=="__main__":   
    app.run(debug=True)    