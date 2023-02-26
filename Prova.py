from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return ('<h1>Hello, world!</h1>')

@app.route('/chisono')
def nome():
    return ('<h1>riccardo</h1>')

@app.route('/file')
def file():
  return render_template("introduzione.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)