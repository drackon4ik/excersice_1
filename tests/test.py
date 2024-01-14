# Процессы являются контейнерами. Их основная задача – изолировать программы друг от друга,
# чтобы одна не могла получить доступ к памяти другой.

# Потоки – интерфейсы работы с процессами и потоками в Python очень похожи.
# Потоки живут внутри процессов, потребляют меньше ресурсов и разделяют общую память внутри процесса.

# decorators
# декоратор это обвертки вокруг функций или классов котороя меняет их поведение
# обычно декораторы используется для декорирования функций

# class Rectangle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     @property
#     def area(self):
#         return self.a * self.b
#
# rect = Rectangle(5, 6)
# print(rect.area)
# 30

# @property это функция, которая принимает другую функцию в качестве аргумента и возвращает ещё одну функцию
# @property позволяет не вызывать метод area, а обращаться как к атрибуту(без использования скобок -> ())


# import time
#
#
# def retry(func):
#     def _wrapper(*args, **kwargs):
#         try:
#             func(*args, **kwargs)
#         except:
#             time.sleep(1)
#             func(*args, **kwargs)
#
#     return _wrapper
#
#
# @retry
# def might_fail():
#     print("might_fail")
#     raise Exception
#
#
# might_fail()

# если при 1 вызове функции произошел сбой, нужно вызвать декоратор @retry для повторного вызова (обычно 1 или 2 раза)
# @retry принимает любую функцию как аргумент, и определяет новую функцию _wrapper после чего ее возвращает
# функция _wrapper видна только внутри пространства имен декоратора (@retry)
# при вызове @retry нет круглых скобок, потому что при вызове might_fail мы вызываем на самом деле
# @retry которому передается функция в виде 1 аргумента


# class C:
#     @staticmethod
#     def the_static_method(arg1, arg2):
#         return 42
#
# print(C.the_static_method())

# @staticmethod нужен если хотим вызвать функцию, определенную внутри класса не создавая экземпляр класса


# from datetime import date
#
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # a class method to create a
#     # Person object by birth year.
#     @classmethod
#     def FromBirthYear(cls, name, year):
#         return cls(name, date.today().year - year)
#
#     def display(self):
#         print("Name:", self.name, " Age:", self.age)
#
#
# person = Person('Max', 18)
# person.display()
# выведет -> Name: Max Age: 18
# person1 = Person.FromBirthYear('Denis', 1999)
# person1.display()
# выведет -> Name: Denis Age: 24
# @classmethod функция которая отнимает год рождения от текущего года (2023 - 1999 = 24)


# контекстные менеджеры
# with open("file.txt", "r") as file:
# data = file.read()
# действия с данными
# файл автоматически закрывается после выхода из блока

# Контекстные менеджеры предоставляют удобство и безопасность при работе с файлами, базами данных, и т.д


# import time
#
#
# class Timer:
#     def __enter__(self):
#         self.start_time = time.time()
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         elapsed_time = time.time() - self.start_time
#         print(f"Elapsed time: {elapsed_time} seconds")
#
#
# Пример использования контекстного менеджера
# with Timer() as timer:
#     # Ваш блок кода
#     time.sleep(2)

# __enter__() выполняется перед выполнением блока кода внутри оператора with. Он может выполнять какие-либо
# подготовительные действия или возвращать значение, которое будет связано с переменной после ключевого слова as
# __exit__() вызывается после завершения выполнения блока кода with. Он используется для выполнения завершающих действий
# таких как освобождение ресурсов, обработка исключений или выполнение финализирующих операций.


# list comprehensions
# list_using_comp = [n*2 for n in range(5)]
# print(item)
# [0, 2, 4, 6, 8]

# dict comprehension
# dict_using_comp = {n: n*2 for n in range(5)}
# print(item)
# {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

# set comprehensions
# input_list = [1, 2, 3, 4, 5, 6, 7]
# set_using_comp = {var for var in input_list if var % 2 == 0}
# print(set_using_comp)
# {2, 4, 6}

# lambda функции
# x = lambda a, b : a * b
# print(x(5, 6))
# 30

# умножает 5 на 6 = 30


# *args
# def function(*args):
#     for i in args:
#         print(i)


# print(function(1, 2, 3, 4))
# выведет -> 1
#            2
#            3
#            4

# *args используется для передачи неопределенного числа неименованных аргументов,
# Если поставить звездочку перед именем то будет представлять собой кортеж из всех переданный аргументов функции


# **kwargs
# def function(**kwargs):
#     for name, value in kwargs.items():
#         print(f'{name} = {value}')


# print(function(a=1, b=2, c=3))
# выведет -> a = 1
#            b = 2
#            c = 3

# **kwargs -> работает так же, как и *args, но вместо кортежа используется словарь,
# позволяет функции принимать любое количество именованных аргументов, и обязательно поставить ** перед именем, не *


# exceptions, try-except

# Определение функции, которая пытается поделить число на ноль
# def divide(x, y):
#     result = x / y
#     return result
# try:
#     result = divide(5, 0)
#     print(f"Result of dividing {x} by {y}: {result}")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# Cannot divide by zero.

# концепция работы try-except
# try:
#     попробуй сделать все что тут написано
# except название ошибки которая может встретиться, и игнорировать ее что бы не сломала код:
#    и выведи альтернативу что бы код все равно запустился, но не была ошибка в терминале после запуска кода


# PEP(Python Enhancement Proposal), PEP8 и PEP484

# PEP8,является официальным стандартом написания кода на Python. Этот документ содержит рекомендации и правила,
# которым стоит следовать, чтобы ваш код был легко читаемым, понятным и единообразным.


# def split_integer(number, parts):
#     # Step 1: Divide 'number' by 'parts' to fimd the quotient and remainder
#     quotient, remainder = divmod(number, parts)
#
#     # Step 2: Calculate the number of parts that will receive the quotient
#     base_parts_counts = parts - remainder
#
#     # Step 3: Create an array of integers where each element is the quotient
#     base_parts = base_parts_counts * [quotient]
#
#     # Step 4: create an array of integers where each element is the quotient + one
#     extra_parts = remainder * [quotient + 1]
#
#     # Step 5: Combine the two arrays from steps 3 and 4, return
#     return base_parts + extra_parts

# from functools import wraps
# import time
#
#
# def timeit(func):
#     @wraps(func)
#     def timeit_wrapper(*args, **kwargs):
#         start_time = time.perf_counter()
#         result = func(*args, **kwargs)
#         end_time = time.perf_counter()
#         total_time = end_time - start_time
#         print(f'Function {func.__name__} Took {total_time:.2f} seconds and {total_time/60:.2f} minutes')
#         return result
#     return timeit_wrapper
#
#
# @timeit
# def calculate(num):
#     total = sum((x for x in range(0, num**2)))
#     return total
#
#
# if __name__ == '__main__':
#     calculate(5000)
#     calculate(6000)
#
#
# nums = [i for i in range(10)]
# print(nums)

# 1
# lst = ['abc', 'xyz', 'aba', '1221']
# for i in lst:
#     if i[0] == i[-1]:
#         print(i)

# 2
# nums = [1, 'c', 3, 'v', 5]
# letters = [2, 'b', 3, 'r']
#
# for i in nums:
#     if i not in letters:
#         print("No difference")
#     elif i in letters:
#         print("There is a difference")

# 3
# nums = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# new_lst = []
# for i in nums:
#     if type(i) == int:
#         new_lst.append(i)
#     if type(i) == list:
#         for j in i:
#             new_lst.append(j)
# print(new_lst)


# 4
# nums = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# new_nums = []
# [[10, 20], [30, 56, 25], [33], [40]]
# for i in nums:
#     for j in i:
#         new_nums.append(j)
# print(list(set(new_nums)))


# 5
# dct = {'c1': 'Red', 'c2': 'Green', 'c3': None}
# for key, value in dct.copy().items():
#     if value is None or value == '':
#         del dct['c3']
# print(dct)

# 6
# nums = [{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
# for i in nums:
#     for key, value in i.items():
#         i[key] = int(value)
#
#
# decimal_nums = [{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]
# for j in decimal_nums:
#     for key, value in j.items():
#         j[key] = float(value)
# print(decimal_nums)


# 7
# dict1 = {'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
# dict2 = {'x': 300, 'y': 'Red', 'z': 600}
# dict3 = {}
#
#
# def dict_combine(p):
#     for key, value in p.items():
#         if key in dict3:
#             dict3[key].append(value)
#         else:
#             dict3[key] = [value]
#
#
# dict_combine(dict1)
# dict_combine(dict2)
# print(dict3)
# {'w': [50], 'x': [100, 300], 'y': ['Green', 'Red'], 'z': [400, 600]}


# Inheritance super() from Parent class
# class Parent():
#     def __init__(self, age):
#         self.age = age
#
#     def output(self):
#         print(f"Hello, I am {self.age} years old")
#
#     def __str__(self):
#         print("Yes")
#
#
# class Child(Parent):
#     def __init__(self, age, ):
#         super().__init__(age)
#
#
# x = Child(17)
# x.output()


# abstract method decorator
# from abc import ABC, abstractmethod
#
#
# class Polygon(ABC):
#
#     @abstractmethod
#     def noofsides(self):
#         pass
#
#
# class Triangle(Polygon):
#
#     # overriding abstract method
#     def noofsides(self):
#         print("I have 3 sides")
#
#
# class Pentagon(Polygon):
#
#     # overriding abstract method
#     def noofsides(self):
#         print("I have 5 sides")
#
#
# class Hexagon(Polygon):
#
#     # overriding abstract method
#     def noofsides(self):
#         print("I have 6 sides")
#
#
# class Quadrilateral(Polygon):
#
#     # overriding abstract method
#     def noofsides(self):
#         print("I have 4 sides")
#
#
# # Driver code
# R = Triangle()
# R.noofsides()
#
# K = Quadrilateral()
# K.noofsides()
#
# R = Pentagon()
# R.noofsides()
#
# K = Hexagon()
# K.noofsides()


# polymorphysm using the same function name but different signature
# len() being used for a string
# print(len("geeks"))
#
# len() being used for a list
# print(len([10, 20, 30]

# 1
# numbers = [1, 1, 2, 3, 4]
# no_duplicates = set(numbers)

# 2
# num = [1, 2, 3, 4, 5]
# setted = set(num)
# for i in setted:
#     power_of = i ** 2

# 3
# num = [1, 2, 3, 4, 5]
# setted = set(num)
# add_num = setted.add(6)

# 4
# num = [1, 2, 3, 4, 5]
# setted = set(num)
# remove_num = setted.remove(4)

# 5
# numbers = [0, 1, 2, 3, 4, 5]
# no_duplicates = set(numbers)
# no_duplicates.remove(4)
# print(no_duplicates)

# 6
# setx = {"green", "blue"}
# sety = {"blue", "yellow"}
# setz = setx & sety
# print(setz)

# class Base:
#     def __init__(self):
#         self.a = "GeeksforGeeks"
#         self.__c = "GeeksforGeeks"
#
#
# # Creating a derived class
# class Derived(Base):
#     def __init__(self):
#         # Calling constructor of
#         # Base class
#         Base.__init__(self)
#         print("Calling private member of base class: ")
#         print(self.__c)
#
#     # Driver code
#
#
# obj1 = Base()
# print(obj1.a)

# multiple inheritence examples
# class SuperClass:

# def super_method(self):
#     print("Super Class method called")


# define class that derive from SuperClass
# class DerivedClass1(SuperClass):
#     def derived1_method(self):
# print("Derived class 1 method called")


# define class that derive from DerivedClass1
# class DerivedClass2(DerivedClass1):

# def derived2_method(self):
#     print("Derived class 2 method called")


# create an object of DerivedClass2
# d2 = DerivedClass2()

# d2.super_method()  # Output: "Super Class method called"

# d2.derived1_method()  # Output: "Derived class 1 method called"

# d2.derived2_method()  # Output: "Derived class 2 method called"


# inputs = [
#     "John",
#     "Smith",
#     "United states",
#     "Blue",
#     "Brown",
#     28
# ]
#
# first, last, *_, age = inputs
# print(f"{first} {last} is {age} years old")

# import requests


# def wikidata_scraper(url):
#     id =
#     label =
#     description =
#
#
#     return {
#         "ID": None,
#         "LABEL": None,
#         "DESCRIPTION": None,
#     }


# 1
# import datetime

# today = datetime.datetime(2024, 3, 15)

# weekday = today.weekday()

# print([day for day in range(today.day - (weekday - 0), (today.day + (7 - weekday)))])

# start_date = today - datetime.timedelta(days=weekday)

# end_date = start_date + datetime.timedelta(days=6)

# dates = [start_date + datetime.timedelta(days=i) for i in range(7)]

# print("The dates of the current week are:")
# for date in dates:
#     print(date.strftime("%Y-%m-%d"))

# 2
# import datetime
# import pytz
# 
# time_utc = datetime.datetime(2024, 1, 6, 12, 17, 30)
#
# timezone = pytz.timezone('Europe/Madrid')
#
# time = time_utc.astimezone(timezone)
#
# print("UTC time:", time_utc)
# print(f"{timezone} time:", time.strftime('%Y-%m-%d %H:%M:%S'))
