from flask import Flask

application = Flask(__name__)

@application.route('/')
def index():
    return "Meh."

if __name__ == "__main__":
    application.run(host='0.0.0.0')
