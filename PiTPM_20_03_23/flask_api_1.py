from flask import Flask

app = Flask(__name__)

@app.route('/home/')
def index():
    return 'Home Page'

@app.route('/career/')
def career():
    return 'Career Page'

# несколько URL для одной функции представления

@app.route('/contact/')
@app.route('/feedback/')
def feedback():
    return 'Feedback Page'

# путь с динамическим элементом
@app.route('/user/<int:id>/') # в примере неверно
def user_profile(id):
    return "Profile page of user #{}".format(str(id))



if __name__ == "__main__":
    app.run(debug=True)