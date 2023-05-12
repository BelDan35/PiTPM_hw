from flask import *
app = Flask(__name__, static_folder="static")

@app.route('/')
def index():
    name = "Jerry"
    template_context = dict(name=name)
    return render_template('index.html', **template_context)

  
@app.route('/admin') 
def admin(): 
    return 'admin' 
  
@app.route('/librarion') 
def librarion(): 
    return 'librarion' 
  
@app.route('/student') 
def student(): 
    return 'student' 
  
@app.route('/user/<name>') 
def user(name): 
    if name == 'admin': 
        return redirect(url_for('admin')) 
    if name == 'librarion': 
        return redirect(url_for('librarion', genre='biography', page=2, sort_by='date-published')) 
    if name == 'student': 
        return redirect(url_for('student')) 

app.run()