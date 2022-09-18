from operator import index
from flask import Flask, render_template 

#----------------------------1-halloworld
app = Flask(__name__)    
@app.route('/')           
def hello_world():
    # return render_template('index.html')
    return "<h1 style='display:flex; color:red justify-content:center '> Hello World </h1>" 



# @app.route('/success')
# def success():
#     return render_template("index.html")
#----------------------------2-Dojo
@app.route('/Dojo') 
def dojo():
    return "Dojo! " 
#----------------------------3-name
@app.route('/say/<name>') 
def hello(name):
    print(name)
    return "Hi " + name


#----------------------------4--repeat
@app.route('/rpeat/<intg>/<nam>')  
def say_int(nam, intg):
    return "<br>hi "+ nam*int(intg)

if __name__=="__main__":   
    app.run(debug=True)    



