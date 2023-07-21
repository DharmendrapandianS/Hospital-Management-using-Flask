from flask import *

app = Flask(__name__)

@app.route('/')
def home1():
    my_name = "WELCOME TO MAFIZ"
    return render_template("home1.html", your_name = my_name)

@app.route('/signup')
def signup():
    ku ="ENTER YOUR NAME"
    juu = "AGE"
    return render_template("signup.html",annu = ku, mannu = juu)

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/admlogin')
def admlogin():
    return render_template("admlogin.html")

@app.route('/doclogin')
def doclogin():
    return render_template("doclogin.html")

@app.route('/booking')
def booking():
    return render_template("booking.html")


@app.route('/help')
def help():
    return render_template("help.html")

@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")

# @app.route('/exit')
# def exit():
#     return redirect(url_for("help"))

if __name__ == "__main__":
    app.run(debug = True)


