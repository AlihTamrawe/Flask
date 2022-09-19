from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    print(request.form)
    straw = request.form['strawberry']
    rasp = request.form['raspberry']
    apple = request.form['apple']
    student_id = request.form['student_id']
    first_name = request.form['first_name']
    last_name = request.form['last_name']

    the_result = str(int(straw)+int(rasp)+int(apple))
    return render_template("checkout.html",the_result=the_result,straw=straw,rasp=rasp,apple=apple,student_id=student_id,first_name=first_name,last_name=last_name)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    