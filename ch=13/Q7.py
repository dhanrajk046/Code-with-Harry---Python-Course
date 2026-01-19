from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run()

# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Hello, Flask!"

# if __name__ == "__main__":
#     app.run(debug=True)
