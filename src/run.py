import bcrypt
from functools import wraps
from flask import Flask, render_template, redirect, request, session, url_for
from flask import Flask
app = Flask(__name__, template_folder='/home/tc/Nicky_Brownlie_set09103_coursework2/src/templates')

from data import *

app.secret_key = 'A0Zr98j /3 yX R~XHH!jmN]LWX /,? RT '

valid_email = 'admin@admin'
valid_pwhash = bcrypt.hashpw('admin', bcrypt.gensalt())

def check_auth(email, password):
  if(email == valid_email and valid_pwhash == bcrypt.hashpw(password.encode('utf-8'), valid_pwhash)):
        return True
  return False

def requires_login(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        status = session.get('logged_in', False)
        if not status:
          return redirect(url_for('.root'))
        return f(*args, **kwargs)
    return decorated

@app.route('/logout/')
def logout():
    session['logged_in'] = False
    return redirect(url_for('.root'))

@app.route("/admin/")
@requires_login
def secret():
  var1 = LeafandBean
  return render_template('adminpage.html', var1=var1)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['email']
        pw = request.form['password']

        if check_auth(request.form['email'], request.form['password']):
          session['logged_in'] = True
          return redirect(url_for('.secret'))
    return render_template('login.html')

@app.route('/')
def root():
  return render_template('homepage.html')

@app.route('/allcoffee/')
def allcoffee():
  return render_template('allcoffee.html', LeafandBean=LeafandBean,
                                           LaBarantine=LaBarantine,
                                           ThePod=ThePod,
                                           Starbucks=Starbucks,
                                           Costa=Costa,
                                           ProjectCoffee=ProjectCoffee,
                                           OrganicDeliciousCafe=OrganicDeliciousCafe,
                                           CafeNero=CafeNero,
                                           Greggs=Greggs,
                                           PieceBox=PieceBox)

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
