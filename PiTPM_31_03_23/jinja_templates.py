from jinja2 import *

# Определение выражения

print(Template("{{ 10 + 3 }}").render())
print(Template("{{ 10 - 3 }}").render())
print(Template("{{ 10 // 3 }}").render())
print(Template("{{ 10 / 3 }}").render())
print(Template("{{ 10 % 3 }}").render())
print(Template("{{ 10 ** 3 }}").render())

# Вывод переменных

print(Template("{{ var }}").render(var=12))
print(Template("{{ var }}").render(var="hello"))
print(Template("{{ var[1] }}").render(var=[1,2,3]))
print(Template("{{ var['profession'] }}").render(var={'name':'tom', 'age': 25, 'profession': 'Manager' }))
print(Template("{{ var[2] }}").render(var=("c", "c++", "python")))

class Foo:
    def __str__(self):
        return "This is an instance of Foo class"
    
print(Template("{{ var }}").render(var=Foo()))

# обращение к несуществующему индексу

print(Template("{{ var[100] }}").render(var=("c", "c++", "python"))) # ''

# Вызов функции

def foo():
    return "foo() called"

print(Template("{{ foo() }}").render(foo=foo))

# Атрибуты и методы

class Foo:
    def __init__(self, i):
        self.i = i
    def do_something(self):
        return "do_something() called"

print(Template("{{ obj.i }}").render(obj=Foo(5)))
print(Template("{{ obj.do_something() }}").render(obj=Foo(5)))


# Создание шаблона из стороннего файла

max_score = 100
test_name = "Python Challenge"
students = [
    {"name": "Sandrine",  "score": 100},
    {"name": "Gergeley", "score": 87},
    {"name": "Frieda", "score": 92},
    {"name": "Fritz", "score": 40},
    {"name": "Sirius", "score": 75},
]

# Пример с шаблоном .txt

environment = Environment(loader=FileSystemLoader("jTemplate/"))
template = environment.get_template("message.txt")

for student in students:
    filename = f"message_{student['name'].lower()}.txt"
    content = template.render(
        student,
        max_score=max_score,
        test_name=test_name
    )
    with open(filename, mode="w", encoding="utf-8") as message:
        message.write(content)
        print(f"... wrote {filename}")


# Пример с шаблоном .html

template2 = environment.get_template("index.html")
results_filename = "index_rendered.html"

context = {
    "students": students,
    "test_name": test_name,
    "max_score": max_score,
}
with open(results_filename, mode="w", encoding="utf-8") as results:
    results.write(template2.render(context))
    print(f"... wrote {results_filename}")