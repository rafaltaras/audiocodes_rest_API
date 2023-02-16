from flask import Flask, render_template, request, url_for, redirect, flash, abort
from lib.endpoints import config
from lib.dto import dto

app = Flask(__name__)

@app.route("/", methods=["GET"])
def mainpage():
    data = request.args
    if not data:
        return render_template("mainpage.html")
    ip = data.get('ip')
    username = data.get('username')
    password = data.get('password')
    dto.config = config.download_config(ip, username, password)
    path = dto.config
    all_sections = config.read_ini(path)
    filtered_sections = config.filter_sections(all_sections)
    config.create_docx_file(ip,path,filtered_sections)
    return render_template("config_sections.html",sections=filtered_sections, ip=ip)
    
@app.route("/config_details/<section>")
def config_details(section):
    if not dto.config:
        abort(404)
    parameter_details = config.read_parameter_details(dto.config, section)
    config_details = config.create_ini_dict(parameter_details)
    return render_template("config_details.html", config_details=config_details, section=section)
  
@app.route("/certificate/")
def certificate():
    # data = request.args
    # ip = data.get('ip')
    # username = data.get('username')
    # password = data.get('password')
    return "Option under construction"

@app.route("/license/")
def license():
    return "Option under construction"

@app.route("/alarms/")
def alarms():
    return "Option under construction"

@app.route("/update/")
def update():
    return "Option under construction"

if __name__ == '__main__':
    app.run(debug=True)