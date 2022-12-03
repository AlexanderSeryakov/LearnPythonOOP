"""Объявите класс LinkedList (связный список) для работы со следующей структурой данных:

Здесь создается список из связанных между собой объектов класса ObjList. Объекты этого класса создаются командой:

obj = ObjList(data)
где data - строка с некоторой информацией. Также в каждом объекте obj класса ObjList должны создаваться следующие
локальные атрибуты:

__data - ссылка на строку с данными;
__prev - ссылка на предыдущий объект связного списка (если объекта нет, то __prev = None);
__next - ссылка на следующий объект связного списка (если объекта нет, то __next = None).

В свою очередь, объекты класса LinkedList должны создаваться командой:

linked_lst = LinkedList()
и содержать локальные атрибуты:

head - ссылка на первый объект связного списка (если список пуст, то head = None);
tail - ссылка на последний объект связного списка (если список пуст, то tail = None).

А сам класс содержать следующие методы:

add_obj(obj) - добавление нового объекта obj класса ObjList в конец связного списка;
remove_obj(indx) - удаление объекта класса ObjList из связного списка по его порядковому номеру (индексу); индекс
отсчитывается с нуля.

Также с объектами класса LinkedList должны поддерживаться следующие операции:

len(linked_lst) - возвращает число объектов в связном списке;
linked_lst(indx) - возвращает строку __data, хранящуюся в объекте класса ObjList, расположенного под индексом indx
(в связном списке)."""


class ObjList:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, prev):
        self.__prev = prev


class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def add_obj(self, obj):
        if self.tail:
            self.tail.next = obj
        obj.prev = self.tail
        self.tail = obj
        if not self.head:
            self.head = obj

    def remove_obj(self, indx):
        if not self.head:
            return None
        if not self.head.next:
            self.head = None
            self.tail = None
            return
        pointer = self.head
        while pointer:
            if not indx:
                if pointer == self.head:
                    self.head = self.head.next
                    self.head.prev = None
                    return
                if pointer == self.tail:
                    self.tail = self.tail.prev
                    self.tail.next = None
                    return
                pointer.prev.next = pointer.next
                pointer.next.prev = pointer.prev
                return
            else:
                pointer = pointer.next
                indx -= 1
        else:
            print('Указан неверный индекс')

    def __len__(self):
        pointer = self.head
        len_lst = 0
        if pointer:
            while pointer:
                pointer = pointer.next
                len_lst += 1
        else:
            return 0
        return len_lst

    def __call__(self, indx, *args, **kwargs):
        pointer = self.head
        while pointer:
            if not indx:
                return pointer.data
            pointer = pointer.next
            indx -= 1
        else:
            print('Неверно указан индекс')

nodes_lst = [ObjList('data1'), ObjList('data2'), ObjList('data3')]

linked_lst = LinkedList()
for obj in nodes_lst:
    linked_lst.add_obj(obj)

assert linked_lst.head.data == 'data1', 'Неверно добавлены узлы связанного списка'
assert linked_lst.tail.data == 'data3', 'Неверно добавлены узлы связанного списка'

ln = LinkedList()
ln.add_obj(ObjList("Александр"))
ln.add_obj(ObjList("Серяков"))
ln.add_obj(ObjList("Python ООП"))
ln.remove_obj(2)
assert len(ln) == 2, "функция len вернула неверное число объектов в списке, возможно, неверно работает метод remove_obj()"
ln.add_obj(ObjList("Python"))
assert ln(2) == "Python", "неверное значение атрибута __data, взятое по индексу"
assert len(ln) == 3, "функция len вернула неверное число объектов в списке"
assert ln(1) == "Серяков", "неверное значение атрибута __data, взятое по индексу"

n = 0
h = ln.head
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__next
    n += 1

assert n == 3, "при перемещении по списку через __next не все объекты перебрались"

n = 0
h = ln.tail
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__prev
    n += 1

assert n == 3, "при перемещении по списку через __prev не все объекты перебрались"
