#houses_history = []

class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
            return
        for floor in range(1, new_floor+1):
            print(floor)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        """должен возвращать True, если количество этажей одинаковое у self и у other."""
        if not isinstance(other, House):
            return False
        return other.number_of_floors == self.number_of_floors

    def __lt__(self, other):
        if not isinstance(other, House):
            return False
        return other.number_of_floors < self.number_of_floors

    def __le__(self, other):
        if not isinstance(other, House):
            return False
        return other.number_of_floors <= self.number_of_floors

    def __gt__(self, other):
        if not isinstance(other, House):
            return False
        return other.number_of_floors > self.number_of_floors

    def __ge__(self, other):
        if not isinstance(other, House):
            return False
        return other.number_of_floors >= self.number_of_floors

    def __ne__(self, other):
        if not isinstance(other, House):
            return False
        return other.number_of_floors != self.number_of_floors

    def __add__(self, value):
        """- увеличивает кол-во этажей на переданное значение value, возвращает сам объект self."""
        self.number_of_floors += value
        return self

    def __radd__(self, value):
        """- работают так же как и __add__ (возвращают результат его вызова)."""
        return self + value

    def __iadd__(self, value):
        """- работают так же как и __add__ (возвращают результат его вызова)."""
        return self + value


def test2():
    h1 = House('ЖК Эльбрус', 10)
    h2 = House('ЖК Акация', 20)

    print(h1)
    print(h2)

    print(h1 == h2)  # __eq__

    h1 = h1 + 10  # __add__
    print(h1)
    print(h1 == h2)

    h1 += 10  # __iadd__
    print(h1)

    h2 = 10 + h2  # __radd__
    print(h2)

    print(h1 > h2)  # __gt__
    print(h1 >= h2)  # __ge__
    print(h1 < h2)  # __lt__
    print(h1 <= h2)  # __le__
    print(h1 != h2)  # __ne__
"""
Вывод на консоль:
Название: ЖК Эльбрус, кол-во этажей: 10
Название: ЖК Акация, кол-во этажей: 20
False
Название: ЖК Эльбрус, кол-во этажей: 20
True
Название: ЖК Эльбрус, кол-во этажей: 30
Название: ЖК Акация, кол-во этажей: 30
False
True
False
True
False
"""

def test1():
    h1 = House('ЖК Эльбрус', 10)
    h2 = House('ЖК Акация', 20)

    # __str__
    print(h1)
    print(h2)

    # __len__
    print(len(h1))
    print(len(h2))

"""
Вывод на консоль:
Название: ЖК Эльбрус, кол-во этажей: 10
Название: ЖК Акация, кол-во этажей: 20
10
20
"""


def test0():
    h1 = House('пещера', -2)
    h1.go_to(0)
    h1.go_to(-1)
    h1.go_to(-2)
    h1.go_to(-3)

    h2 = House('_______________', 0)
    h2.go_to(1)
    h2.go_to(0)
    h2.go_to(-1)
    h2.go_to(-100)

    h3 = House('', 2)
    h3.go_to(0)
    h3.go_to(1)
    h3.go_to(2)
    h3.go_to(3)


def test3():
    h1 = House('ЖК Эльбрус', 10)
    print(House.houses_history)
    h2 = House('ЖК Акация', 20)
    print(House.houses_history)
    h3 = House('ЖК Матрёшки', 20)
    print(House.houses_history)

    # Удаление объектов
    del h2
    del h3

    print(House.houses_history)
    """
    Вывод на консоль:
    ['ЖК Эльбрус']
    ['ЖК Эльбрус', 'ЖК Акация']
    ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
    ЖК Акация снесён, но он останется в истории
    ЖК Матрёшки снесён, но он останется в истории
    ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
    ЖК Эльбрус снесён, но он останется в истории
    """


#test0()
#test1()
#test2()
test3()





"""
2023/11/02 00:00|Домашняя работа по уроку "Различие атрибутов класса и экземпляра."
Если вы решали старую версию задачи, проверка будет производиться по ней.
Ссылка на старую версию тут.

Цель: понять разницу между атрибутами объекта и класса, дополнив уже существующий класс. Применить метод __new__.

Дополнительно о работе метода __new__:
Как мы уже знаем метод __new__ вызывается перед тем, как вызовется метод __init__.
Разберёмся, как происходит передача данных между ними на следующем примере:
class Example:
  def __new__(cls, *args, **kwargs):
  print(args)
    print(kwargs)
    return object.__new__(cls)

  def __init__(self, first, second, third):
  print(first)
  print(second)
    print(third)

ex = Example('data', second=25, third=3.14)

Работа __new__:
'data' передаётся (упаковывается) в *args, т.к. это позиционный аргумент. Он будет находиться под индексом 0 как единственный элемент кортежа.
second=25 и third=3.14 передаются (упаковываются) в **kwargs т.к. это именованные аргументы. Они будут находиться под ключами 'second' и 'third' со значением 25 и 3.14 соответственно в словаре.
Передача данных из __new__ в __init__:
После того как метод __new__ отработает до конца, произойдут следующие события с параметрами __init__:
В параметр first распакуется из args единственный аргумент 'data'.
В параметр second распакуется значение под ключом с тем же названием из словаря kwargs.
В параметр third распакуется значение под ключом с тем же названием из словаря kwargs.


Задача "История строительства":
Для решения этой задачи будем пользоваться решением к предыдущей задаче "Перегрузка операторов".

В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.

Правильней вписывать здание в историю сразу при создании объекта, тем более можно удобно обращаться к атрибутам класса используя ссылку на сам класс - cls.
Дополните метод __new__ так, чтобы:
Название объекта добавлялось в список cls.houses_history.
Название строения можно взять из args по индексу.

Также переопределите метод __del__(self) в котором будет выводиться строка:
"<название> снесён, но он останется в истории"

Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__, а также значение атрибута houses_history.

Пример результата выполнения программы:
Пример выполнения программы:
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

Вывод на консоль:
['ЖК Эльбрус']
['ЖК Эльбрус', 'ЖК Акация']
['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
ЖК Акация снесён, но он останется в истории
ЖК Матрёшки снесён, но он останется в истории
['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
ЖК Эльбрус снесён, но он останется в истории

Примечания:
Более подробно о работе метода __new__ можно узнать здесь.
В методе __new__ можно обращаться к атрибутам текущего класса при помощи параметра cls.

Файл module_5_4.py и загрузите его на ваш GitHub репозиторий. В решении пришлите ссылку на него.
"""
