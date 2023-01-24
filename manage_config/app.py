from flask import Flask, render_template, request, url_for, redirect, flash
from lib.endpoints import config

app = Flask(__name__)

@app.route("/", methods=["GET"])
def mainpage():
    data = request.args
    if data:
        ip = data.get('ip')
        username = data.get('username')
        password = data.get('password')
        path = config.download_config(ip, username, password)
        parameters = config.read_ini(path)
        return render_template("config_details.html",parameters=parameters)
    return render_template("mainpage.html")

# @app.route("/details/<path>")
# def config_details(path):
#     parameters = config.read_ini(path)
#     return render_template("config_details.html", parameters = parameters)    

if __name__ == '__main__':
    app.run(debug=True)