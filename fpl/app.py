from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method=="POST":
        id = int(request.form.get("id"))
        return redirect(url_for('login',id=id))        
    return render_template("home.html")

@app.route("/login/<int:id>")
def login(id):
    return f"Hello, {id}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)