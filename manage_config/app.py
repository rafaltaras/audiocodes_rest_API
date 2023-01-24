from flask import Flask, render_template, request
from lib.endpoints import config

app = Flask(__name__)

@app.route("/", methods=["GET"])
def mainpage():
    data = request.args
    if data:
        ip = data.get('ip')
        username = data.get('username')
        password = data.get('password')
        conf = config.download_config(ip, username, password)
        print(conf)
    return render_template("mainpage.html")
    

if __name__ == '__main__':
    app.run(debug=True)