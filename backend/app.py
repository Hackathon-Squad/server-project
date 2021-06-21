from flask import Flask
from dotenv import load_dotenv
from api.routes import api

load_dotenv()

app = Flask(__name__)

app.register_blueprint(api)


@app.route("/")
def hello_world():
    return "Hello World"


if __name__ == "__main__":
    app.run()
