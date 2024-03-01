from flask import Flask, Response,request
from flask import render_template

application = Flask(__name__,static_folder='photo')

@application.route("/", methods=["GET"])
def main():
    user_agent = request.user_agent.string
    if "Mobi" in user_agent:
        return render_template("main(mbi).html")
    else:
        return render_template("main.html")

@application.route("/about", methods=["GET"])
def about():
    user_agent = request.user_agent.string
    if "Mobi" in user_agent:
        return render_template("about(mbi).html")
    else:
        return render_template("about.html")

@application.route("/gallery",methods=["GET"])
def gallery():
    return render_template("gallery.html")

@application.route("/Gallery/<string:k>",methods=["GET"])
def gallery2(k):
    return render_template(f"Gallery/{k}.html")

@application.route("/events",methods=["GET"])
def events():
    user_agent = request.user_agent.string
    if "Mobi" in user_agent:
        return render_template("events(mbi).html")
    else:
        return render_template("events.html")

@application.route("/events1",methods=["GET"])
def events1():
    return render_template("events1.html")

@application.route("/events2",methods=["GET"])
def events2():
    return render_template("events2.html")

@application.route("/events3",methods=["GET"])
def events3():
    return render_template("events3.html")

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000, ssl_context=('path/to/cert.pem', 'path/to/key.pem'))
