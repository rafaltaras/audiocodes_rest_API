from flask import Flask, render_template, request
from lib.endpoints import config

app = Flask(__name__)

# ip = 
# username = "Admin"
# password = "Admin"


@app.route("/", methods=["GET"])
def mainpage():
    data = request.args
    if data:
        ip = data.get('ip')
        username = data.get('username')
        password = data.get('password')
        conf = config.get_config(ip, username, password)
    return render_template("mainpage.html")
    

if __name__ == '__main__':
    app.run(debug=True)