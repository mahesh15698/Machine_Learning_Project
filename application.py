from flask import Flask

application = Flask(__name__)
app = application


@app.route("/", methods=['GET','POST'])
def index():
    return "starting machine learning project"

if __name__ == '__main__':
    app.run(debug=True)