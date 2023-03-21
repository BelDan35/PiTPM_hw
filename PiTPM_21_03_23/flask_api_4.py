from flask_api_2 import app
from flask import request, current_app


with app.test_request_context('/books'):
    print(request.path) # получим полный путь к запрашиваемой странице(без домена).
    print(request.method)
    print(current_app.name)