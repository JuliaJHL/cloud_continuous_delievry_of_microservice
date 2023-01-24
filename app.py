from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    """return an HTTP greeting and login interface."""
    return render_template("login.html")


@app.route('/login', methods=["post"])
def login():
    user_name = request.form.get("user_name")
    user_pwd = request.form.get("user_pwd")
    if user_name == "IDS721" and user_pwd == "DUKE2023":
        return "Login successful!"
    else:
        return "Login failed!"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

