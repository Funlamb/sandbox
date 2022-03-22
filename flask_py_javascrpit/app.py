from crypt import methods
from pkgutil import extend_path
from flask import Flask, redirect, render_template, request, session
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.secret_key = "toots"

@app.route("/")
def home():
    return render_template("form.html")

if __name__ == '__main__':
   app.run()