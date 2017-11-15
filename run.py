from flask import Flask, render_template
app = Flask(__name__, template_folder='/home/tc/Nicky_Brownlie_set09103_coursework2/src/templates')

from src.data import *

@app.route('/coffee/leafandbean/')
def coffeepage():
  var1 = LeafandBean
  return render_template('coffee.html', var1=var1)

if __name__==("__main__"):
  app.run(host='0.0.0.0', debug=True)
