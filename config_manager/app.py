from flask import Flask, render_template, request, url_for, redirect, flash, abort
from lib.endpoints import config
from lib.dto import dto

app = Flask(__name__)
# app.jinja_env.globals.update(isinstance=isinstance)
# app.jinja_env.globals.update(list=list)


@app.route("/", methods=["GET"])
def mainpage():
    data = request.args
    if not data:
        return render_template("mainpage.html")
    ip = data.get('ip')
    username = data.get('username')
    password = data.get('password')
    dto.config = config.download_config(ip, username, password)
    dto.sections = config.read_ini(dto.config)
    config.create_docx_file(ip)
    return render_template("config_details.html",sections=dto.sections)
    
@app.route("/parameter_details/<section>")
def parameter_details(section):
    if not dto.config:
        abort(404)
    parameter_details = config.read_parameter_details(dto.config, section)
    print(type(parameter_details))
    param_details = config.create_ini_dict(parameter_details)
    print(type(param_details))
    return render_template("parameter_details.html", param_details=param_details, section=section)
  

if __name__ == '__main__':
    app.run(debug=True)