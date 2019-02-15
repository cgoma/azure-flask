from flask import Flask
app = Flask(__name__)

@app.route('/home')
def hello_world():
    return '<br><h1>Hello, World of Chetan Vijay Gomase!</h1>'
if __name__ == "__main__":
    app.run()
