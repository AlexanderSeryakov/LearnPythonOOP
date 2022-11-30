""" Необходимо объявить класс-декоратор с именем Handler, который можно было бы применять к функциям следующим образом:

@Handler(methods=('GET', 'POST')) # по умолчанию methods = ('GET',)
def contact(request):
    return "Сергей Балакирев"
Здесь аргумент methods декоратора Handler содержит список разрешенных запросов для обработки. Сама декорированная
функция вызывается по аналогии с предыдущим подвигом:

res = contact({"method": "POST", "url": "contact.html"})
В результате функция contact должна возвращать строку в формате:

"<метод>: <данные из функции>"

В нашем примере - это будет:

"POST: Сергей Балакирев"

Если ключ method в словаре request отсутствует, то по умолчанию подразумевается GET-запрос. Если ключ method принимает
значение отсутствующее в списке methods декоратора Handler, например, "PUT", то декорированная функция contact должна
возвращать значение None.

Для имитации GET и POST-запросов в классе Handler необходимо объявить два вспомогательных метода с сигнатурами:

def get(self, func, request, *args, **kwargs) - для имитации обработки GET-запроса
def post(self, func, request, *args, **kwargs) - для имитации обработки POST-запроса

В зависимости от типа запроса должен вызываться соответствующий метод (его выбор в классе можно реализовать методом
__getattribute__()). На выходе эти методы должны формировать строки в заданном формате.

P.S. В программе достаточно объявить только класс. Ничего на экран выводить не нужно.

Небольшая справка
Для реализации декоратора с параметрами на уровне класса в инициализаторе __init__(self, methods) прописываем параметр
для декоратора, а магический метод __call__() объявляем как полноценный декоратор на уровне функции, например:

class Handler:
    def __init__(self, methods):
        # здесь нужные строчки

    def __call__(self, func):
        def wrapper(request, *args, **kwargs):
            # здесь нужные строчки
        return wrapper
"""


class Handler:
    def __init__(self, methods=('GET', )):
        self.methods = methods

    def __call__(self, func, *args, **kwargs):
        def wrapper(request, *args, **kwargs):
            if 'method' not in request.keys() or request['method'] == 'GET' and request['method'] in self.methods:
                return self.get(func, request)
            elif request['method'] == 'POST' and request['method'] in self.methods:
                return self.post(func, request)

        return wrapper

    def get(self, func, request, *args, **kwargs):
        return f"GET: {func(request)}"

    def post(self, func, request, *args, **kwargs):
        return f"POST: {func(request)}"


assert hasattr(Handler, 'get') and hasattr(Handler, 'post'), "класс Handler должен содержать методы get и post"

@Handler(methods=('GET', 'POST'))
def contact2(request):
    return "контакты"

assert contact2({"method": "POST"}) == "POST: контакты", "декорированная функция вернула неверные данные"
assert contact2({"method": "GET"}) == "GET: контакты", "декорированная функция вернула неверные данные"
assert contact2({"method": "DELETE"}) is None, "декорированная функция вернула неверные данные"
assert contact2({}) == "GET: контакты", "декорированная функция вернула неверные данные при указании пустого словаря"

@Handler(methods=('POST',))
def index(request):
    return "index"

assert index({"method": "POST"}) == "POST: index", "декорированная функция вернула неверные данные"
assert index({"method": "GET"}) is None, "декорированная функция вернула неверные данные"
assert index({"method": "DELETE"}) is None, "декорированная функция вернула неверные данные"


@Handler(methods=('GET',))
def index2(request):
    return 'index2'

assert index2({'method': 'POST'}) is None, "декорированная функция вернула неверные данные"
