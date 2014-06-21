from flask import Flask
from flask import render_template, url_for
import png
app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template('base.html', home=home)

@app.route('/<hex>')
def get_color(hex=None):
	return render_template('color.html', hex=hex)

# url_for('static', filename='style.css')

if __name__ == '__main__':
  app.run()