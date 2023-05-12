from flask import *
app = Flask(__name__)


@app.route('/user/<name>')
def user(name): 
    if name == 'admin': 
        return redirect(url_for('admin')) 
    if name == 'librarion': 
        return redirect(url_for('librarion', genre='biography', page=2, sort_by='date-published')) 
    if name == 'student': 
        return redirect(url_for('student')) 
  
@app.route('/admin') 
def admin(): 
    return 'admin' 
  
@app.route('/librarion') 
def librarion(): 
    return 'librarion' 
  
@app.route('/student') 
def student(): 
    return 'student' 


app.run()