from flask import Flask
from flask import render_template

app= Flask(__name__)  # tomado de https://desarrolloweb.com/faq/desde-python-enlace-web-hacia-html

@app.route('/')
def index():
     return render_template("index.html")
  #    return render_template('index.html')
if __name__== '__main__':
     app.run(debug=True)