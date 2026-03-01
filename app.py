from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
  return '''
Main page<br>
<a href="/about">О компании</a><br>
<a href="/hello/Programmist">Привет</a>
'''

@app.route('/about')
def about():
  return 'This is the about page'

@app.route('/hello/<name>')
def hello(name):
  return render_template('hello.html', name=name)

if __name__ == '__main__':
  app.run(debug=True)
