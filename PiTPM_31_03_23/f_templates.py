# Отрисовка шаблонов с помощью render_template()

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name, age, profession = "Jerry", 24, 'Programmer'
    template_context = dict(name=name, age=age, profession=profession)

    return render_template('index.html', **template_context)

# Отрисовка шаблонов в консоли

from jinja2 import *

@app.route('/jinja')
def index2():
    t = Template("Name: {{ name }}")
    t.render(name='Jerry')


app.run()