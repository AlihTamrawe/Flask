from itertools import count
from operator import index
from time import time
from turtle import color
from unicodedata import name
from flask import Flask, render_template , request,session ,redirect

#----------------------------1-halloworld

app = Flask(__name__)    
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def create():
    if 'name' in session:
        print('key exists!')
        
    else:
        print("key 'key_name' does NOT exist")
        session['name'] =0
    count = session['name']
    count+=1
    session['name']=count
    return render_template('index.html',t=session['name'])
@app.route('/destroy')
def dest():
    print("Got Post Info")
    if 'name' in session:
        print('key exists!')
        session['name'] =0 
    else:
        print("key 'key_name' does NOT exist")
        session['name'] =0
    return redirect('/')
    
    








if __name__=="__main__":   
    app.run(debug=True)    

