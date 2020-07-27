from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "This is a Homepage!"

if __name__ == "__main__":
    app.run()
    