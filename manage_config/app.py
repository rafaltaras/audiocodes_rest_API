from flask import Flask, render_template, request, url_for, redirect, flash
from lib.endpoints import config

app = Flask(__name__)

@app.route("/", methods=["GET"])
def mainpage():
    data = request.args
    if not data:
        return render_template("mainpage.html")
    ip = data.get('ip')
    username = data.get('username')
    password = data.get('password')
    path = config.download_config(ip, username, password)
    sections = config.read_ini(path)
    return render_template("config_details.html",sections=sections)
    
@app.route("/parameter_details/<section>")
def parameter_details(section):
    parameter_details = config.read_parameter_details(section)
    return render_template("parameter_details.html")
  

if __name__ == '__main__':
    app.run(debug=True)