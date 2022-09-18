from operator import index
from time import time
from turtle import color
from flask import Flask, render_template 

#----------------------------1-halloworld

app = Flask(__name__)    
@app.route('/')           
def normal():
    return render_template("index.html" ,times=3,color='blue')


@app.route('/play/<int:time>')           
def play(time):
    return render_template("index.html", times=time,color='blue')


@app.route('/play/<int:time>/<color>')           
def play_color(time,color):
    return render_template("index.html", color=color, times=time)
 




if __name__=="__main__":   
    app.run(debug=True)    

