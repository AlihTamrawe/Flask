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
    users_info = [
   {'id':1,'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'id':2,'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'id':3,'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'id':4,'first_name' : 'KB', 'last_name' : 'Tonel'}
] 

    return render_template("index.html", users = users_info)

if __name__=="__main__":   
    app.run(debug=True)    