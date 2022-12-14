"""Часто множественное наследование используют для наполнения дочернего класса определенным функционалом. То есть,
с указанием каждого нового базового класса, дочерний класс приобретает все больше и больше возможностей. И, наоборот,
убирая часть базовых классов, дочерний класс теряет соответствующую часть функционала.

Например, паттерн миксинов активно используют в популярном фреймворке Django.  В частности, когда нужно указать
дочернему классу, какие запросы от клиента он должен обрабатывать (запросы типа GET, POST, PUT, DELETE и т.п.).
В качестве примера реализуем эту идею в очень упрощенном виде, но сохраняя суть паттерна миксинов.

Предположим, что в программе уже существует следующий набор классов:

class RetriveMixin:
    def get(self, request):
        return "GET: " + request.get('url')


class CreateMixin:
    def post(self, request):
        return "POST: " + request.get('url')


class UpdateMixin:
    def put(self, request):
        return "PUT: " + request.get('url')

Здесь в каждом классе выполняется имитация обработки запросов. За GET-запрос отвечает метод get() класса RetriveMixin,
за POST-запрос - метод post() класса CreateMixin, за PUT-запрос - метод put() класса UpdateMixin.

Далее, вам нужно объявить класс с именем GeneralView, в котором следует указать атрибут (на уровне класса):

allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')
для перечня разрешенных запросов. А также объявить метод render_request со следующей сигнатурой:

def render_request(self, request): ...

Здесь request - это словарь (объект запроса), в котором обязательно должны быть два ключа:

'url' - адрес для обработки запроса;
'method' - метод запроса: 'GET', 'POST', 'PUT', 'DELETE' и т. д.

В методе render_request() нужно сначала проверить, является ли указанный запрос в словаре request разрешенным
(присутствует в списке allowed_methods). И если это не так, то генерировать исключение командой:

raise TypeError(f"Метод {request.get('method')} не разрешен.")
Иначе, вызвать метод по его имени:

method_request = request.get('method').lower()  # имя метода, малыми буквами
Подсказка: чтобы получить ссылку на метод с именем method_request, воспользуйтесь магическим методом __getattribute__().

Для использования полученных классов, в программе объявляется следующий дочерний класс:

class DetailView(RetriveMixin, GeneralView):
    allowed_methods = ('GET', 'PUT', )
Воспользоваться им можно, например, следующим образом (эти строчки в программе не писать):

view = DetailView()
html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'GET'})
print(html)   # GET: https://stepik.org/course/116336/
Если в запросе указать другой метод:

html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'PUT'})
то естественным образом возникнет исключение (реализовывать в программе не нужно, это уже встроено в сам язык Python):

AttributeError: 'DetailView' object has no attribute 'put'

так как дочерний класс DetailView не имеет метода put. Поправить это можно, если указать соответствующий базовый класс:

class DetailView(RetriveMixin, UpdateMixin, GeneralView):
    allowed_methods = ('GET', 'PUT', )
Теперь, при выполнении команд:

view = DetailView()
html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'PUT'})
print(html)
будет выведено:

PUT: https://stepik.org/course/116336/

Это и есть принцип работы паттерна миксинов.

P.S. В программе требуется объявить только класс GeneralView. На экран выводить ничего не нужно."""


class RetriveMixin:
    def get(self, request):
        return "GET: " + request.get('url')


class CreateMixin:
    def post(self, request):
        return "POST: " + request.get('url')


class UpdateMixin:
    def put(self, request):
        return "PUT: " + request.get('url')


# здесь объявляйте класс GeneralView

class GeneralView:
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')

    def render_request(self, request):
        if request['method'] not in self.allowed_methods:
            raise TypeError(f"Метод {request.get('method')} не разрешен.")
        return self.__getattribute__(request['method'].lower())(request)


class DetailView(RetriveMixin, UpdateMixin, GeneralView):
    allowed_methods = ('GET', 'POST', )

# Tests

assert issubclass(DetailView, GeneralView), "класс DetailView должен наследоваться от класса GeneralView"


class DetailView(RetriveMixin, UpdateMixin, GeneralView):
    allowed_methods = ('GET', 'POST',)


view = DetailView()

try:
    html = view.render_request({'url': '123', 'method': 'POST'})
except AttributeError:
    assert True
else:
    assert False, "не сгенерировалось исключение AttributeError при вызове команды render_request({'url': '123', 'method': 'POST'}) при разрешенных методах allowed_methods = ('GET', 'POST', )"

try:
    html = view.render_request({'url': '123', 'method': 'PUT'})
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при вызове команды render_request({'url': '123', 'method': 'PUT'}) при разрешенных методах allowed_methods = ('GET', 'POST', )"

html = view.render_request({'url': '123', 'method': 'GET'})
assert html == "GET: 123", "метод render_request вернул неверные данные"


class DetailView(RetriveMixin, UpdateMixin, CreateMixin, GeneralView):
    allowed_methods = ('GET', 'POST',)


view = DetailView()
html = view.render_request({'url': '123', 'method': 'POST'})
assert html == "POST: 123", "метод render_request вернул неверные данные"
