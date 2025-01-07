from flask import Flask, render_template, request, redirect, url_for

from api_id import managerid

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method=="POST":
        id = int(request.form.get("id"))
        return redirect(url_for('login',id=id))        
    return render_template("home.html")

@app.route("/login/<int:id>")
def login(id):
    first_name = managerid(id)[0]
    last_name = managerid(id)[1]

    return render_template("manager.html",first_name=first_name,last_name=last_name)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)