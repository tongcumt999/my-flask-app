#from flask import Flask,render_template,redirect,url_for
from flask import Flask, render_template, redirect, url_for, request

app1 = Flask(__name__)

@app1.route("/")
def fun():
    #return "Hello world!!!....."
    return render_template("index.html")

@app1.route("/about")
def about():
    return render_template("about.html")

@app1.route("/add/<a>/<b>")
def add(a,b):
    return str(int(a)+int(b))

@app1.route("/ctof/<float:c>")
@app1.route("/ctof/<int:c>")
def ctof(c):
    f = float(c)*9/5+32
    return "%2.1f C is %2.1f F"%(c,f)

@app1.route("/admin")
def hello_admin():
    return "hello admin..."

@app1.route("/guest/<guest>")
def hello_guest(guest):
    return "hello %s"%guest

@app1.route("/user/<name>")
def hello_user(name):
    if name=='admin':
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for("hello_guest",guest=name))

@app1.route("/success/<name>")
def success(name):
    return "Hello %s" % name

@app1.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm'] # This 'nm' must match the 'name' attribute in your HTML input
        return redirect(url_for('success', name=user))
    else:
        return render_template("login.html")


if __name__=="__main__":
    app1.run(debug=True)
