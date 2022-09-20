from flask import Flask, render_template, request, redirect # added request

app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    print(request.form)
    return render_template("index.html")


@app.route('/users', methods=['POST'])
def Dojo():
    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['name']
    location_from_form = request.form['location']
    languages_from_form = request.form['languages']
    commment_from = request.form['commment']
    return render_template("show.html",commment=commment_from, name_on_template=name_from_form, languages_on_template=languages_from_form,location_from_form=location_from_form)


if __name__ == "__main__":
    app.run(debug=True)

