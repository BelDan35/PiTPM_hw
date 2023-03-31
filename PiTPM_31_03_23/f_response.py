from flask import Flask, make_response, redirect, g, abort

app = Flask(__name__)


@app.route('/')
def main():
    print("index() called")
    return 'Testings Request Hooks'

# Создание ответа с помощью make_response()

@app.route('/404')
def http_404_handler():
    return make_response("404 Error", 400)

@app.route('/books/<string:genre>/')
def books(genre):
    res =  make_response("All Books in {} category".format(genre))
    res.headers['Content-Type'] = 'text/plain'
    res.headers['Server'] = 'Foobar'
    return res

@app.route('/set-cookie')
def set_cookie():
    res = make_response("Cookie setter")
    res.set_cookie("favorite-color", "red", 60*60*24*5)
    res.set_cookie("favorite-font", "sans-serif", 60*60*24*5)
    return res


# Создание ответов с помощью кортежей

@app.route('/500')
def http_500_handler():
    return ("500 Error", 500) # или return "500 Error", 500

# заголовки с помощью кортежей

@app.route('/Heading')
def render_markdown():
    return "## Heading", 200, {'Content-Type': 'text/markdown'}

# перенаправление пользователя

@app.route('/transfer')
def transfer():
    # return "", 302, {'location': 'https://localhost:5000/login'} # №1
    # return redirect("https://localhost:5000/login") # №2
    # указываем другой статус код
    return redirect("https://localhost:5000/login", code=301)


# Перехват запросов

@app.before_first_request
def before_first_request():
    print("before_first_request() called")

@app.before_request
def before_request():
    print("before_request() called")

@app.after_request
def after_request(response):
    print("after_request() called")
    return response

# Отмена запроса с помощью abort()

@app.route('/abort')
def abort():
    abort(404)

# Изменение страниц ошибок

@app.errorhandler(404)
def http_404_handler(error):
    return "HTTP 404 Error Encountered", 404

@app.errorhandler(500)
def http_500_handler(error):
    return "HTTP 500 Error Encountered", 500

if __name__ == "__main__":
    app.run(debug=True)