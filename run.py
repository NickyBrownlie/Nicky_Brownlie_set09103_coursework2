from flask import Flask, render_template
app = Flask(__name__, template_folder='/home/tc/Nicky_Brownlie_set09103_coursework2/src/templates')

from src.data import *

@app.route('/leafandbean/')
def leafandbean():
  var1 = LeafandBean
  return render_template('coffee.html', var1=var1)

@app.route('/labarantine/')
def labarantine():
  var1 = LaBarantine
  return render_template('coffee.html', var1=var1)

@app.route('/thepod/')
def thepod():
  var1 = ThePod
  return render_template('coffee.html', var1=var1)

@app.route('/starbucks/')
def starbucks():
  var1 = Starbucks
  return render_template('coffee.html', var1=var1)

@app.route('/costa/')
def costa():
  var1 = Costa
  return render_template('coffee.html', var1=var1)

@app.route('/projectcoffee/')
def projectcoffee():
  var1 = ProjectCoffee
  return render_template('coffee.html', var1=var1)

@app.route('/organicdeliciouscafe/')
def organicdeliciouscafe():
  var1 = OrganicDeliciousCafe
  return render_template('coffee.html', var1=var1)

@app.route('/cafenero/')
def cafenero():
  var1 = CafeNero
  return render_template('coffee.html', var1=var1)

@app.route('/greggs/')
def greggs():
  var1 = Greggs
  return render_template('coffee.html', var1=var1)

@app.route('/piecebox/')
def piecebox():
  var1 = PieceBox
  return render_template('coffee.html', var1=var1)


if __name__==("__main__"):
  app.run(host='0.0.0.0', debug=True)
