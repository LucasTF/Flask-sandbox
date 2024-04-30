from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/dashboard")
def dashboard():
    return "<h1>Dashboard</h1>"

if __name__ == "__main__":
    app.run(debug=True)