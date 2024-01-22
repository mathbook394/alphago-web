from flask import Flask, Response
from flask import render_template

app = Flask(__name__,static_folder='photo')

@app.route("/", methods=["GET"])
def main():
    return render_template("main.html")

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")

@app.route("/gallery",methods=["GET"])
def gallery():
    return render_template("gallery.html")

@app.route("/Gallery/<string:k>",methods=["GET"])
def gallery2(k):
    return render_template(f"Gallery/{k}.html")

@app.route("/events",methods=["GET"])
def events():
    return render_template("events.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
