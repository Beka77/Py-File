# it_company= ["IT RUN","GEEKTECH","OLOLO","BI SOFT"]
# print(it_company)
# it_company.append("ITS")
# it_company.append("it_companyITS BOOTCAMP")
# print(it_company)
# it_company.insert(2, "NEW IT")
# print(it_company)

# print(it_company[1:4])

# from statistics import mean


# from statistics import mean


# numbers = [1, 10, 5, 7, 100, 200, 100000,5000]
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))
# print(len(numbers) / sum(numbers))
# print(mean(numbers))



# num1 = float(inpnum1 = int(input("Num1: "))
# num2 = int(input("Num2: "))
#     print(num1 + num2)ut("Num1: "))
# num2 = float(input("Num2: "))
# print(num1 + num2)


# numbers = [20, 1, 2, 5, 500, 3, 1000, 10.05]
# numbers.sort()
# print(numbers)

# it_company = ["IT RUN","GEEKTECH", "OLOLO", "BI SOFT","Alam"]
# it_company.reverse()
# print(it_company)

# for i in range(10, 20, 2):
#     print(i)

# n = 0 
# while True:
#     n += 1
#     print(n)
#     if n == 100:
#         break

# numbers = [10, 12, 11, 1, 7, 2, 3, 500, 600]
# for it in numbers:
#     if it % 2 == 0:
#         print("Четные число" , it)
#     else:
#         print("Нечетное число" , it)

# numbers = [10, 12, 11, 1, 7, 2, 3, 500, 600]
# for i in numbers:
#     print(i)
#     if i == 10:

# n = o 
# while True: 
#     n +=1
#     print (n)
#     if n == 10000:
#         break 

# a = 10 
# b = 20 
# while a < b: 
#         a += 1 
#         print(a)

# password1 = input ("Введите новый пароль")
# password2 = input("Подтвердите пароль")
# passwords = []
# if password1 == password2:
#     passwords.append(password1)
#     if len(passwords[-1]) < 8:
#         print("Пароль короткий и легкий")
#     elif "123" in passwords[-1]:
#         print("Простой и легкий")
#     else: 
#         print("Ok")
# else:
#     print("Пароли различаются")  

# print(10 / 0)


# from xml.dom import HierarchyRequestErr


# try:
#     print(10 + "Hello")
# except BaseException:
#     print("У вас ошибка")

# hello = "Hi"
# try:
#     print(hi)
# except NameError:
#     raise TypeError("IT RUN")
# finally:
#     print("Ошибка типов данных! Иди читай notion")

# names = [1 ,1.0 ,"Hello", True, ['IT' ,'RUN']]
# print(names)
# names = {10 ,2.0 , True, ("IT", "Hello")}
# print(names)

# cars = {"Audi", "BMW", "TESLA", "Rolls Royce"}
# cars.add("Test")
# print (cars)
# cars.pop()
# print(cars)
# cars.remove("TESLA")
# print(cars)

# for i in cars:
#        print(i)

# cars = frozenset({1, 2, 3, 4, 4, 4})
# for i in cars:
#     print(i)

# numbers = []
# for i in range(1, 1000001):
#     numbers.append(i)
#     print(i)

# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))
# # print(i)

# import numbers

# import numbers


# numbers = [1, 2, 3, 4, 5]


# 5) Пользователь вводит три числа. Если все числа больше 10, то вывести на экран yes, иначе no
# num1 = int(input("Enter 1num: "))
# num2 = int(input("Enter 2num: "))
# num3 = int(input("Enter 3num: "))
# if num1 > 10 and num2 > 10 and num3 > 10:
#     print("Yes")
# else:
#     print("No")

# 6) Дано три числа. Найти количество положительных чисел среди них
# num1 = input("Enter 1num: ")
# num2 = input("Enter 2num: ")
# num3 = input("Enter 3num: ")
# print(f'{3-(num1+num2+num3).count("-")}')



# 7) Пользователь вводит количество месяцев и лет. Вывести на экран количество дней 
# за это время. Считать, что в каждом месяце 29 дней;




# from builtins import input


# year = int(input("Year: "))
# month = int(input("Month: "))
# total = (year * 348) + (month * 29)
# print(total, "дней прошло")

# 9) Напишите программу отбора в военкомат. Если Алмазу меньше 16ти лет то должно вывести 
# "еще рано", если 18 и выше то вывести "идем служить", 
# а если возраст равна 40 и выше то вывести "уже не надо"
# from builtins import input


# almaz = int(input("Введи свой возраст: "))
# if almaz < 16:
#     print("еще рано")
# elif almaz == 18 or almaz >18:
#     print("идем служить")
# elif almaz == 40 and almaz > 40:
#     print("уже не надо")

# 1) Напишите код, который спрашивает имя и фамилию пользователя. Сделайте так
# чтоб на экран вышла первая буква имена, точка и фамилия полностью с приветствием.
# Вывод: Здравствуйте К. Токторов!
# name = input("Введите имя: ")
# surname = input("Введите фамилию: ")
# print(f"Здравствуйте {name[0]}. {surname}")

# 2) Сделайте мини калькулятор, который находит только сумму двух данных
# пользователям чисел и выводит на экран с надписью
# Вывод на терминале: - Сумма равна: *сумма двух чисел*
# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# print(f"Сумма равна: {num1 + num2}")

# 3) Программа должна попросить ввести любую строку нижнем регистре. Задача вашей
# программы вывести на экран все символы в данной строке в верхнем регистре.

# stroka = input("Введите имя: ")
# print(stroka.title())
# # 4)Есть текст:
# text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
# tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
# nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute
# irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
# Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit
# anim id est laborum."""
# print(text.count("e"))


# Ваша задача, вывести на экран количество символов в данном тексте и
# вывести количество буквы „e“ в данной программе.

# 5) Найдите периметр(p) и площадь(s) квадрата , попросив пользователя ввести длину
# квадрата. Попробуйте тоже самое сделать для прямоугольника стороны квадрата.

# Периметр квадрата
# a = int(input("Введите сторону квадрата: "))
# print(f"Перимметр квадарат равен: {a * 4}")

# Площадь квадрата
# a = int(input("Введите сторону квадрата: "))
# print(f"Площадь квадарат равен: {a * a}")


# Периметр прямоугольника
# a = int(input("Введите длину прямоугольника: "))
# b = int(input("Введите ширина прямоугольника: "))
# result = (a + b) * 2
# print(f"Периметр прямоугольника равен: {result}")

# # Площадь прямоугольника
# a = int(input("Введите длину прямоугольника: "))
# b = int(input("Введите ширина прямоугольника: "))
# result = a * b
# print(f"Площадь прямоугольника равен: {result}")

# for i in range(1, 6):
#     print(f"0 - {i}")

# lst = []
# for i in range(1, 101):
#     lst.append(i)

# print(lst)

# for i in range(1, 498):
#     if i % 2 == 0:
#         print(i)

# lst = []
# for i in range(1, 10000001):
#     lst.append(i)
# print(min(lst))
# print(max(lst))
# print(sum(lst))

# lst = []
# for i in range(1, 101):
#     lst.append('0')
# print(lst)


# student = dict(name = "Muntasir", age = 19, study = "IT RUN")
# print(student)


#student = {"Name" : "Muntasir", "age" : 18, "study" : "IT RUN"}
# print (student)
# del student["age"]
# print(student)
# print (student["age"])
# student.setdefault("Hello")
# student.pop("Name")

# student = {"Name" : "Muntasir", "age" : 18, "study" : "IT RUN"}
# student ['study'] = "OSH MU"
# student['color']
# print (student)


# marks = {'Physicks':67, 'Maths':87}
# internal_marks = {'Practical':48}
# marks.update(internal_marks)
# print(marks)

# student = {"Name" : "Muntasir", "age" : 18, "study" : "IT RUN"}
# new_dict = student.copy()
# print(new_dict)
# print(student.keys())
# print(student.values())
# print(student.get('color'))
# print(student.items())
 

# contact = {"Muntasir" : 996777777777}
# while True:
#     command = input("1 - искать, 2 - добавить, 3 - удалить, 4 - обновить номер, 5 - посмотреть все контакты: ")
#     if command == "1":
#         find_num = input("Какой контакт вы хотите найти? ")
#         if find_num in contact:
#             print("Есть", contact[find_num])
#         else:
#             print("Такого нету")
#     elif command == "2":
#         add_name = input("Кого добавить? ")
#         add_num = input("Введите номер: ")
#         contact.setdefault(add_name, add_num)
#         print("Контакт успешно добавлен")
#     elif command == '3':
#         delete_contact = input("Кого хотите удалить  ? ")
#         if delete_contact in contact:
#             contact.pop(delete_contact)
#             print(f"Такого {delete_contact} контакта не существует")

#     elif command == '4':
#         update_con = input("Чей номерм хотите обновить ? ")
#         update_tel = input("На какой номер хотите изменить ? ")
#         if update_con in contact:
#             contact[update_con] = update_tel
#             print("Номер успешно обновлен")
#         else:
#             print(f"Такого {update_con} контакта не существует")

#     elif command== '5':
#         for key,value in contact.items():
#             print(f"{key} - {value}")
#     else:
#         print("Такого команды нету")

# Для чего нужны исключения(try, except)?
# Чтобы слваливать ошибки и форматировать их под себя

# Словите ошибку ZeroDivisionError  и выведите “Делить на ноль нельзя! Ты чо вася”
# a = 10
# b = 0
# try:
#     print(a / b)
# except ZeroDivisionError:
#     print("Делить на ноль нельзя! Ты чо вася")

# Словите ошибку TypeError и выведите “Ошибка типов данных! Иди читай notion”
# a = 15
# b = 15
# try:
#     print(a + b)
# except TypeError:
#     print("Ошибка типов данных! Иди читай notion")
# finally:
#     print("CHITAY NOTION !")

# Дайте пользователю ввести две отметки времени вместе с секундами. Ваша
# программа должна найти разницу между двумя отрезками времени и вывести
# на экран в секундах.
# **Условие: Первая отметка должна быть раньше по времени чем вторая.**
# Пример:
# 1-ввод: 10:00:30
# 2-ввод: 15:05:09
# Ответ: 18 279 секунд разница


# Вывестите на экран все четные числа в диапазоне от 1 до 400 и запишите в пустой список
# chet_num = []
# for i in range(1, 401):
#     if i % 2 == 0:
#         chet_num.append(i)
# print(chet_num)


# a = 100 
# b = 20
# if a > b:
#     print("А больше всех")
# else:
#     print("А не больше всех") 

# a = 100
# b = 10
# res = "А больше всех" if a > b else "А меньше всех"
# print(res)


# a = 100
# b = 10
# print("А больше всех" if a > b else"А меньше всех")

# a = 100
# b = 10
# c = 1000
# if c > b and c > a:
#     print("С больше всех")
# if b < a and b < c:
#     print("В меньше всех")


# a = 100
# b = 10
# c = 1000
# res = a if a > b and a > c else b if b > a and b > a and c
# print (res)

# number = int(input("Number: "))
# if number % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")


# number = int(input("Number: "))
# print("Четное" if number % 2 == 0 else "Нечетное")

# number = int(input("Number: "))
# print(('Четное', 'Нечетное')[number % 2])


# from ast import Num


# num = []
# for i in range(0, 101):
#     num.append(i)

# print(num)




# num = [i for i in range (0, 101)]
# print(num)


# num = []
# for i in range(0, 101):
#     if i % 2 == 0:
#         num.append(i)


# print(num)

# num = [i for i in range(0, 101) if i % 2 == 0]
# print(num)

# petrol = {
#     'Ai 100' : 50,
#     'Ai 95' : 55,
#     'Ai 92' : 50,
#     'Ai 80' : 40,
#     'DT' : 30,
# }
# new_petrol = { k:v + 10 for k, v in petrol.items()}
# print(new_petrol)

# new_petrol = {}
# for key, value in new_petrol.items():
#     new_petrol.setdefault(key, value + 10)
# print(new_petrol)

# for key, value in petrol.items():
#     if value == 50:
#         petrol[key] = value + 5
        
        
# print(petrol)

# lst = []
# for i in range(10):
#     lst.append(i)
# print(lst)

# num = [i for i in range (10)]
# print(num)

# lst = []
# for i in range (10):
#     if i % 2 == 0:
#         lst.append(i)
# print(lst)


# lst = [i for i in range (10) if i % 2 == 0]
# print(lst) 

# cars = {"Audi", "BMW", "TESLA", "Rolls Royce"}
# car = []
# for x in cars:
#     if "A" in x: 
#         car.append(x)
#         print(car)

# car = [x for x in cars if "A" in x]
# print(car)

# squares = []
# for i in range(10):
#     squares.append(i)
# print(squares)

# squares = [i for i in range(10)]
# print(squares)

# range3 = [num * 3 for num in range (1, 6)]
# print(range3)

# range_elements = []
# for num in range(1, 6):
#     a = num * 3 
#     range_elements.append(a)
# print(range_elements)



# a = [1, 10, 12, 4, 3, 20, 55,]

# a_filtered= [num for num in a if num < 10]
# print(a_filtered)

# a_filtered_squared = [num ** 2 for num in a if num < 10]
# print(a_filtered_squared)


# wordss = ['hello', 'world', 'goodbye', 'privet', 'piano', 'qwertyuiopasd']
# words_filtered = [word for word in words if len(word) < 5] 
# print(words_filtered)

# words = [word + '.' for word in wordss if len(word) == 13]
# print(words)

# a = ['first', 1, 2, 3, 'second', 10, 20, 'third', 15, 56, 70, 'fourth', -50]
# d = {}
# b = None
# for el in a:
#     if type(el) == str:
#         d[el] = []
#         b = el 
# print(d) 
#     else:
#         d[b].append(el)
# print(el)


# def hello():
#     print("Hello World")
#     print(10 + 10)
#     print(10 * 2)
# hello()

# def add():
#     num1 = int(input("Num1: "))
#     num2 = int(input("Num2: "))
#     print(num1 + num2)
# add()

# def sub(num1, num2):
#     print(num1 - num2)
# sub(100, 10)

# def chet():
#     numbers = [i for i in range(1000)]
#     for i in numbers:
#         if i % 2 == 0:
#             print(i)
# chet()

# def info(name = "Ivan", surname = "Ivanov"):
#     print(f"Имя {name}, фамилия {surname}")
# info()
# info("Muntasir", "Tolbaev")
# info("Faha", "Hi")

# Создать функцию calc(a, b, operation). Описание входных параметров:
# Первое число(дробное число)
# Второе число(дробное число)
# Действие над ними:
#    1) + Сложить
#    2) - Вычесть
#    3) * Умножить
#    4) / Разделить
#    Сделайте момент где если пользователь делит число на 0, нужно вывести “На ноль делить нельзя”
#    В остальных случаях функция должна возвращать "Операция не поддерживается

# from builtins import input


# def calc(a, b, operation):
#     if operation == "+":
#         print(a + b)
#     if operation == "-":
#         print(a - b) 
#     if operation == "*":
#         print(a * b)
#     if operation == "/":
#         print(a /b)

# a=float(input("Введите значение x ="))
# b=float(input("Введите значение y ="))   
# z=input("Введите оператор (+, -, /, *, mod, pow, div) =")   


# age = int(input("Enter your age: "))

# message = ""

# if age < 18:
# 		message = "Forbidden"
# else:
# 		message = "Welcome"

# print(message)

# 
# def names(*args):
#     print(args)




# names = ("Kurmanbek", "Muntasir", "Diana", "Faha", "IT RUN")

# def elon_musk(name, *company):
#     print(name)
#     for i in company:
#         print(i)

# elon_musk("Elon", "Tesla", "Space X", "PayPal", "Starlink")


# from fnmatch import translate

# def translate(**words):
#     for k, v in words.items():
#         print(k, v)
# translate(USA = "США", Kyrgyzstan = "Кыргызстан")

# def add(num1, num2):
#     print(num1 + num2)
# add(10,10)

# add_sum = lambda num1, num2: num1 + num2 
# print(add_sum(10, 10))

# print((lambda num1, num2: num1 + num2)(10, 10))

# numbers = [1, 2, 3, 4, 5]
# lst = []
# def two(n):
#     for i in n:
#         lst.append(i * 2)
# two(numbers)
# print(lst)

# numbers = [1, 2, 3, 4, 5]
# lst = list(map(lambda n : n * 2, numbers))
# print(lst)

# import numbers


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_lst = []
# def filt(lst):
#     for i in lst:
#         if i % 2 == 0:
#             new_lst.append(i)
#     print(new_lst)

# filt(numbers)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# filt_lambda = list(filter(lambda lst: lst % 2 == 0, numbers))
# print(filt_lambda)

# def hello(x):
#     print (x * x)
# hello(5)

# hello_lambda = lambda x: x * x
# print(hello_lambda(2))


# names = ["Kuma", "Nurtilek", "Zina", "Edzen", "Kuma", "Aitenur", "Zina" ]
# set_name = list(set(map(lambda x: x, names)))

# print(set_name)

# names = ["azat", "zina", "kuma", "anna", "sas"] 
# filt_names = list(filter(lambda x: x == x [::-1], names))
# print(filt_names)


# def add(num1, num2):
#     print(num1 + num2)

# def mult(num1, num2):
#     print(num1 * num2)

# def sub(num1, num2):
#     print(num1 - num2)

# def div(num1, num2):
#     print(num1 / num2)


# def fes():
#     a = int(input("Введите сторону квадрата: "))
#     print(f"Перимметр квадарат равен: {a * 4}")

# def ght():
#     lst = [1, 2, 3, 4 ,5, 6, 7, 8, 9, 10]
#     lst.reverse()
#     print(lst)


# def wev():
#     menu = {
#     "beefstrogonof": 350,
#     "burger": 200,
#     "meatloaf": 500,
#     "chicken pot pie": 400,
#     "beefshteks": 650
# }
#     new_menu= { k:v + 50 for k, v in menu.items()}
#     print(new_menu)


# f = open('lesson.txt', 'w')
# f.write("IT RUN")
# f.close()

# f = open('lesson.txt', 'a+')
# f.write("IT RUN\n")
# f.close()

# it = open ('lesson.txt', 'r', encoding="UTF-8")
# print(it.read())
# it.close

# text = "Киргизия – гористая страна в Центральной Азии. Она расположена вдоль Великого шелкового пути – древней торговой дороги между Китаем и Средиземноморьем. В горах Тянь-Шань, которые окружают этот караванный путь и занимают большую часть страны, обитают снежные барсы, рыси и овцы. На юге страны находится город Ош, история которого насчитывает более тысячи лет. Он славится огромным базаром, где когда-то останавливались купцы, следовавшие по Великому шелковому пути"

# k = open('kyrgyzstan.txt', 'w', encoding='UTF-8')
# k.write(text)
# k.close()

# with open('kyrgyzstan.txt', 'r') as f:
#     print(f.read())

# with open('kyrgyzstan.txt', 'w', encoding='UTF-8') as it:
#     it.write("Hello World")


# with open('kyrgyzstan.txt', 'r', encoding='UTF-8') as hello:
#     print(hello.read())

# n = 0 
# while True:
#     n += 1
#     with open(f'it{n}.py', 'w') as f:
#         f.write(f"print('Hello{n}')")
#     if n == 10:
#         break

# У нас есть переменная text которая, хранит в себе текст:
# Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularized in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
# Откройте файл text.txt и запишите текст в файл(сперва без with, потом с with)

# text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularized in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

# k = open('text.txt', 'w', encoding='UTF-8')
# k.write(text)
# k.close()

# with open('text.txt', 'w', encoding='UTF-8') as it:
#     it.write(text)


# Написать программу, которая откроет созданный в задаче 2 файл text.txt, скопирует весь текст и запишет его в новый файл wikipedia.txt . (с помощью with, потом без
    # wikipedia.txt = ""

    # hp = open('text.txt', 'r', encoding='utf-8')
    # hello = hp.read()
    # print(hello)
    # hp = open('wikipedia.txt', 'w', encoding='utf-8')
    # hp.write(hello)
    # hp.close()

    # with open('text.txt', 'r',encoding='utf-8') as jk:
    #     g = jk.read()
    # with open('wikipedia.txt', 'w', encoding='utf-8') as lk:
    #     lk.write(g)

# Написать программу, которая откроет созданный в задаче 1 файл text.txt, скопирует весь текст и запишет его в новый файл hello.txt . После этого необходимо в новый файл добавить следующий текст: The Kyrgyz, a Muslim Turkic people, constitute more than half the population. The history of the Kyrgyz in what is now Kyrgyzstan dates at least to the 17th century. Kyrgyzstan, known under Russian and Soviet rule as Kirgiziya, was conquered by tsarist Russian forces in the 19th century. Formerly a constituent (union) republic of the U.S.S.R., Kyrgyzstan declared its independence on August 31, 1991. При этом не удаляйте имеющийся текст в файле wikipedia.txt . После этого выведите на экран весь текст данного файла. Задачу решить 2 способами (с with и без with). 
 
# chhh = """\n The Kyrgyz, a Muslim Turkic people, constitute more than half the population. The history of the Kyrgyz in what is now Kyrgyzstan dates at least to the 17th century. Kyrgyzstan, known under Russian and Soviet rule as Kirgiziya, was conquered by tsarist Russian forces in the 19th century. Formerly a constituent (union) republic of the U.S.S.R., Kyrgyzstan declared its independence on August 31, 1991."""

# with open('text.txt', 'r') as test:
#     ds = test.read()
# with open('helo.txt', 'w') as furrea:
#     furrea.write(ds)
# with open('helo.txt', 'a+') as fddd:
#     fddd.write(chhh)

# def it_run():
#     def hello_world():
#         print("Hello World")
#     hello_world()

# it_run()

# def hello():
#     return "Hello"

# print(hello())

# def wrapper(func):
#     def hello():
#         print("Начало декоратора")
#         func()
#         print("Конец декоратора")
#     return hello

# @wrapper
# def test():
#     print("Проверка декоратора")

# test()


# def check(func):
#     def wrapper():
#         func()
#         print("Декоратор")
#     return wrapper

# @check 
# def check_password():
#     password = '2020itrun'
#     password_input = input("Password: ")
#     if password == password_input:
#         print("OK")
#     else:
#         print(None, "В доступе отказано")

# check_password()



# def decorator(func):
#     def wrapper():
#         print("Код до выполнения функции")
#         func()
#         print("Код после выполнения функции")
#     return wrapper

# @decorator
# def show():
#     print("Я обычная функция")

# show()

# def valuetor(func):
#     def wrapper(mes):
#         print("тест до выполнения функции")
#         func(mes)
#         print("текст после выполнения функции")
#     return wrapper

# @valuetor
# def message(mes):
#     print(mes)
#     print("Вот твое сообщение")

# message('Че там')


# def make(func):                     #==> def make(func): 
#     def inmake():                    #        def inner(): 
#         print('Идем играть')        #            print('Идем играть') 
#         func()                      #            func() 
#     return inmake                    #        return inner 
#                                     # @make 
# def kun():                          # def kun(): 
#     print('lets go')                #   print('Lets go') 
#                                     #kun() 
# make(kun)()


              
                   
                   
 
# def smart_divide(func):
#     def inner(a, b):
#         print(f" Я собираюсь разделить {a} и {b} ")
#         if a == 0 or b == 0:
#             print("на ноль делить нельзя")
#         return func(a, b)
#     return inner

# @smart_divide
# def divide(y, n):
#     print(y/n)
# divide(6, 0)

# class Cat:
#     name = "Alisa"
#     age = 10 
#     color = "Black"

#     def say_meoy(self):
#         return "Meoww"

#     def jump(self):
#         return "Cat jump"

#     def info(self):
#         return f"{self.name}, {self.age}, {self.color}"

# cat = Cat() 
# print(cat.name)
# print(cat.say_meoy())
# print(cat.info())

# class Cat:
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color
    
#     def say_meoy(self):
#         return "Meoww"

#     def jump(self):
#         return "Cat jump"

#     def info(self):
#         return f"{self.name}, {self.age}, {self.color}"

# cat = Cat("Alisa", 10, "Black")
# print(cat.info())
# new_cat = Cat("IT", 12, "Black")
# print(cat.info())


# class Car:
#     def __init__(self, brand, model, year, color, volume):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.color = color 
#         self.volume = volume
#         self.odometer = 0
#         self.is_going = False

#     def info(self):
#         return f"{self.brand}, {self.model}, {self.odometer} km, {self.is_going}"    
    
    # def start_engine(self):
    #     self.is_going = True
    #     return f"Автомобиль {self.brand} заведен"

#     def ride(self, km):
#         self.odometer += km
#         return f"двигатель отключен"

#     def stop_engine(self):
#         self.is_going = False
#         return f"Двигатель отключен"
        
# bmw = Car("BMW", "X7", 2022, "White", 7.0)
# tesla = Car("Tesla", "Model X", 2022, "Black", 0)
# print(bmw.info())
# print(tesla.info())
# print(bmw.start_engine())
# print(bmw.info())
# print(bmw.ride(100))
# print(bmw.info())
# print(bmw.stop_engine())
# print(bmw.info())

# class Math:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2 

#     def addition(self):
#         return self.num1 + self.num2
    
#     def multiplication(self):
#         return self.num1 * self.num2

#     def division(self):
#         return self.num1 / self.num2

#     def subtraction(self):
#         return self.num1 - self.num2

# math = Math(5, 2)
# print(math.multiplication())

# class Airplane:
#     def __init__(self, make, model, year, max_speed):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.max_speed = max_speed
#         self.odometer = 0
#         self.is_flying = 0


# class Calculator:
#     def __init__(self):
#         self.window = tk.Tk()

# Self.window.geometry("3375*687")
#     Self.window.resizable

# class Dad:
#     def driver(self):
#         return f"Drive a car"

#     def build(self):
#         return f"Build"
    
# class Mom:
#     def cooking(self):
#         return"Cooking.."

# class Son(Dad, Mom):
#     def programming(self):
# #         return "Coding..."

# # son = Son()
# print(son.driver())
# print(son.build())
# print(son.programming())
# print(son.cooking())


# class VeryOldCar:
#     def engine(self):
#         return "Мотор"

#     def wheeels(self):
#         return "Колесо машин"

# class OldCar(VeryOldCar):
#     def safery_belt(self):
#         return "Ремень безопасности"

# class Car(OldCar):
#     def airbrag(self):
#         return "Подушка безопасности"

# car = Car()
# print(car.airbrag())
# print(car.engine())
# print(car.wheeels())


# Написать класс Person, где у него есть два метода talk, walk. Первый метод talk возвращает “Я могу говорить”. А второй метод walk возвращает “Я могу ходить”.
# class Person:
#     def talk(self):
#         return "Я могу говорить"
#     def walk(self):
#         return "Я могу ходить"

# run = Person()
# print(run.talk())
# Затем вам нужно создать класс Programmer, который наследуется от Person и создать один метод programming, который возвращает “Я могу программировать”.
# class Programmer(Person):
#     def programming(self):
#         return "Я могу программировать"

# kin = Programmer()
# print(kin.programming())

# Потом вам нужно создать еще один класс LittleProgrammer который наследуется от Programmer. Внутри этого класса вам нужно создать метод coding, который возвращает “Я могу писать код”
# class LittleProgrammer(Programmer):
#     def coding(self):
#         return "Я могу писать код"

# ltd = LittleProgrammer()
# print(ltd.coding())
# Затем вам нужно создать еще один класс Builder, который наследуется от Person, и у него есть один метод build, который возвращает “Я могу строить” 
# class Builder(Person):
#     def build(self):
#         return "Я могу строить"

# kdl = Builder()
# print(kdl.build())

# Когда вы все сделали создайте экземпляры классов и используйте все методы
# person = Builder()
# print(person.build())
# print(person.talk())
# print(person.walk())

# person2 = Programmer()
# print(person2.walk())
# print(person2.talk())
# print(person2.programming())

# person3 = LittleProgrammer()
# print(person3.coding())
# print(person3.programming())
# print(person3.walk())
# print(person3.walk())

# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#     def info(self):
#         return f"{self.first_name}, {self.last_name}"

# class Employee(Person):
#     def __init__(self, first_name, last_name, age, status):
#         super().__init__(first_name, last_name, age)
#         self.status = status
#         self.balance = 0

#     def info_about_employee(self):
#         return f"{self.first_name}, {self.status}, {self.balance}"

#     def work(self):
#         self.balance += 1000
#         return f"Work..."

#     def info(self):
#         return super().info() +" "+ str(self.balance)

# employee = Employee("Zalkar", "Kulmamatov", 21, "Manager")
# print(employee.info())
# print(employee.info_about_employee())
# print(employee.work())
# print(employee.info_about_employee())
# print(employee.info())


# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age

#     def info(self):
#         return f"{self.first_name}, {self.last_name}"

# class Bank(Person):
#     def __init__(self, first_name, last_name, age,):
#         super().__init__(first_name, last_name, age)
#         self.balance = 0

#     def earn(self, money):
#         self.balance += money
#         return f"Пополнение"

#     def spend(self, cash):
#         if self.balance > cash:
#             nalog = cash + 5
#             self.balance -= nalog
#             return f"Вывод денег"
#         else:
#             return f"Нету денег"

#     def info(self):
#         return super().info() +  " " + str(self.balance)

# bank = Bank("Zalkar", "kulmamatov",21)
# print(bank.info())
# print(bank.earn(1000))
# print(bank.info())
# print(bank.spend(900))
# print(bank.info())


# age = int(input("Enter your age: "))

# message = ""

# if age < 18:
# 		message = "Forbidden"
# else:
# 		message = "Welcome"

# print(message)

# Напишите класс Washer, которая имитирует поведение стиральной машины. В конструкторе он принимает бренд и цвет машины. И также у него есть переменные, которые мы не передаем powder(начальное значение 0) и is_work(в начальное состояние False). Вам нужно создать методы которые будут имитировать поведение машины. Первый метод start, будет заводить машину и отнимать от powder 20 граммов порошка и делает is_work(True) и также если в powder будет ниже 20, то он должен выводить "Не хватает порошка". Затем вам нужно создать второй метод refuel для заправки вашей стиральной машины. То есть в машину влезет только 100 граммов порошка, не больше. Если вы положили больше 100 граммов, то он должен выводить "В стиралку можно положить лишь 100 грамм порошка". Потом вы должны сделать метод finish, которая отключает стиралку и выводит  "Стиральная машина отключена". И вам все это должны вывести с методом. Создайте экземпляр класса и также используйте все методы.

# class Washer:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
#         self.powder = 0 
#         self.is_work = False
#     def info(self):
#         return f"{self.brand}, {self.color}, {self.is_work}"

#     def start(self):
#         if self.powder < 20:
#             return "Не хватает порошка"
#         else:
#             self.is_work = True
#             self.powder -= 20
#             return "Все работает"

#     def refuel(self, amount):
#         if amount > 100:
#             return "В стиралку можно положить лишь 100 грамм порошка"

#         else:
#             self.powder <+ amount
#             return f"Вы заправили машину на {amount} грамм порошка"

#     def finish(self):
#         self.is_work = False
#         return "Стиральная машина отключена"

# mashina = Washer('Samsung', 'white')
# print(mashina.start())
# print(mashina.refuel(95))
# print(mashina.start())
# print(mashina.finish())

# class Phone:
#     username= "Muntasur"
#     __call_time = 0

#     def call(self):
#         print("Ring Rong")
#         self.__turn_on()
        
#     def __turn_on(self):
#         self.__call_time += 1

#     def info(self):
#         print(f"{self.username} call time {self.__call_time}")

# phone = Phone()
# phone.info()
# phone.call()
# phone.call()
# phone.call()
# phone.info()

# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.__odometer = 0

#     def ride(self, km):
#         self.__odometer += km
#         return f"Вы проехали {km}, и ваш одометер {self.__odometer}"

#     def info(self):
#         return f"{self.brand}, {self.model}, {self.__odometer} km"

# tesla = Car("Tesla", "Model Y", 2021)
# print(tesla.ride(100))
# print(tesla.info())
# print(tesla.ride(100))
# print(tesla.info())
# print(tesla.ride(100000))
# tesla.__odometer = 10000
# print(tesla.info())

# class Student:
#     books = []
#     knowledge = 0
#     is_ready_to_work = False
#     languages = {}

#     def read_book(self):
#         f = input("Какую книгу ты прочитал?")
#         self.books.append(f)
#         self.knowledge += 100
#         return "Книга добавлена"

#     def info(self):
#         return f"Ваши книги: {self.books}, Ваши знания: {self.knowledge} баллов"


# st = Student()
# print(st.read_book())
# print(st.info())
# print(st.do_homework(50))


# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         return f"Dog {self.name}, {self.age}"

#     def make_sound(self):
#         return  "GAwww"

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         return f"Cat {self.name}, {self.age}"

#     def make_sound(self):
#         return  "Meeoow"

# class Cow:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def info(self):
#         return f"Cow {self.name}, {self.age}"

#     def make_sound(self):
#         return  "Muuu"

# dog = Dog("Alabai", 10)
# print(dog.info())
# print(dog.make_sound())

# cat = Cat("Alisa", 14)
# print(cat.info())
# print(cat.make_sound())

# cow = Cow("Mumu", 7)
# print(cow.info())
# print(cow.make_sound())

# dog = Dog("Alabai", 10)
# cat = Cat("Alisa", 14)
# cow = Cow("Mumu", 7)
# for animal in (dog, cat, cow):
#     print(animal.info())
#     print(animal.make_sound())

# from __future__ import annotations


# class Student:
#     def __init__(self, name = "Ivan", groupNumber = "10a", age = "18"):
#         self.name = name
#         self.groupNumber = groupNumber 
#         self.age = age

#     def getName(self):
#         return f"{self.name}"
    
#     def getAge(self):
#         return self.age

#     def getGroupNumber(self):
#         return f"{self.groupNumber}"

#     def setNameAge(self, name, age):
#         self.name = name
#         self.age = age

    
#     def setGroupNumber(self, grnum):
#         self.groupNumber = grnum


# st = Student()
# print(st.getAge())
# print(st.getName())
# st.setNameAge("Bekzat", 14)
# print(st.getAge())
# print(st.getName())
# print(st.getGroupNumber())
# st.setGroupNumber('11b')
# print(st.getGroupNumber())



# Класс Alphabet
# 1. Создайте класс Alphabet
# 2. Создайте метод __init__(), внутри которого будут определены два динамических свойства: 
# 1) lang - язык и
# 2) letters - список букв. Начальные значения свойств берутся из входных параметров метода.
# 3. Создайте метод print(), который выведет в консоль буквы алфавита
# 4. Создайте метод letters_num(), который вернет количество букв в алфавите


# class Alphabet:
#     def __init__(self):
#         def leng(self):

# import string


# class Alphabet:

#     def __init__(self, lang, letters_str):
#         self.lang = lang
#         self.letters = list(letters_str)

#     def print(self):
#         print(self.letters)

  
#     def letters(self):
#         len(self.letters)

# class EngAlphabet(Alphabet):
#     __letters_num = 26
#     def __init__(self):
#         super().__init__('En', string.ascii_uppercase)

#     def is_en_letter(self, letter):
#         if letter.upper() in self.letters:
#             return True
#         return False

#     def letters_num(self):
#         return EngAlphabet.__letters_num

#     def example():
#         print("English Example:\nDon't judge a book by it's cover.")

# eng_alphabet = EngAlphabet()
# eng_alphabet.print()
# print(eng_alphabet.letters())
# print(eng_alphabet.is_en_letter('F'))
# print(eng_alphabet.is_en_letter('Щ'))
# EngAlphabet.example()

# class A:
#     def say_hello(self):
#         print("Hello World")

#     def test1(self):
#         print("It's class A")

# class B:
#     def say_bye(self):
#         print("Bye")

#     def test(self):
#         print("It's class B")

# class C(B, A):
#     def test(self):
#         print("It's class C") 

# c = C()
# c.test1()

# Миксины - это классы, которые ничем не отличаются от обычных. Их главная особенность заключается в том, что они не предназначены для создания экземпляров напрямую. Их основная цель - создать переиспользуемый инструмент, который будет использоваться дочерними для расширения их функционала.

# class EscalatorMixin:
#     def escalator(self):
#         print("It's escalator")

# class LiftMixin:
#     def lift(self):
#         print("It's lift")

# class StairsMixin:
#     def stairs(self):
#         print('It\'s stairs')

# class Building(EscalatorMixin, LiftMixin, StairsMixin):
#     pass 

# building = Building()
# building.lift()
# class Car:
#     def __init__(self, make, model, year, odometer = 0, fuel = 70):
#         self.make = make
#         self.model = model 
#         self.year = year
#         self.odometer = odometer
#         self.fuel = fuel

#     def drive(self, km):
#         self.odometer = km


# from random import randrange
# gg = print("Вывод случайного целого числа ", randrange(1, 11))

# class SlotMachine:
#     def __init__(self, name):
#         self.name = name
#         self.__user_balance = 100
#         self.__game_balance = 0

#     def info(self):
#         return f"{self.name}, {self.__user_balance}, {self.__game_balance}"

#     def top_up_balance(self, money):
#         money = int(input("Сколько денег вы хотите перевести ?"))
#         if self.__user_balance > money:
#             self.__balance_up(money)
#             print("Вы пополнили баланс")
#         else:
#             print("Недостаточно средств")

#     def __balance_up(self, money):
#         self.__user_balance -= money
#         self.__game_balance += money

#     def game(self):
#         n = 0
#         gg = randrange(1, 10)
#         while True:
#             n += 1
#             # print(gg)
#             s = int(input("угадайте число(от 1 до 10), 1 попытка: "))
#             if n == 5:
#                 print("вы проиграли( ")
#                 self.__game_balance -= 10
#                 break
#             elif gg == s

#                 print("вы угадали число")
#                 self.__game_balance += 10
#                 break
#             else:
#                 print("вы не угадали число")


# import random

# class SlotMachine:
#     def __init__(self, name):
#         self.name = name
#         self.__user_balance = 100
#         self.__game_balance = 0

#     def info(self):
#         return f"Имя пользователя: {self.name} | Ваш пользовательский счет: {self.__user_balance} | Ваш игровой счет: {self.__game_balance}"

#     def top_up_balance(self):
#         money = int(input("На какую сумму пополнить ? "))
#         if self.__user_balance > money:
#             self.__balance_up(money)
#             print(f"Вы пополнили счет: {money}")
#         else:
#             print("У вас недостаточно средств")
    

#     def __balance_up(self, money):
#         self.__user_balance -= money
#         self.__game_balance += money


#     def game(self):
#         random_num = random.randint(1, 10)
#         n = 0
#         while True:
#             find_num = int(input("Угадай цифру: "))
#             if find_num >= 1 and find_num <= 10:
#                 n += 1
#                 if n == 5:
#                     print(f"Вы проиграли 10$| Ваш игровой счет: {self.__game_balance}")
#                     self.__game_balance -= 10
#                     break
#                 elif find_num == random_num:
#                     print(f"Вы выиграли 10$| Ваш игровой счет: {self.__game_balance}")
#                     self.__game_balance += 10
#                     break
#                 else:
#                     print(f" Неверно!Осталось попыток–{5-n}")
    
#     def conclusion_money(self):
#         money2 = int(input("Сколько денег вывести ? "))
#         if money2 >= 50:
#             self.__user_balance += money2
#             self.__game_balance -= money2
#         else:
#             print("Вывести можно от 50$")
        
#     def main(self):
#         print(game1.info())
#         game1.top_up_balance()
#         game1.game()
#         game1.conclusion_money()
#         print(game1.info())

# game1 = SlotMachine("Уася")
# game1.main()


# *Абстрактные классы* - это классы, содержащие один или несколько *абстрактных методов*. *Абстрактный метод* - это метод, который создан, но не содержит *имплементации*, не реализован (в методе нет кода).

# От абстрактных классов нельзя напрямую создавать экземпляры. От них можно только наследоваться, и в субклассах необходимо реализовать их методы.

# from abc import ABC,abstractmethod
# class Math(ABC):
#     def __init__(self,a , b):
#         self.a = a
#         self.b= b

#     @abstractmethod
#     def add(self):
#         pass

#     @abstractmethod
#     def sub(self):
#         pass
        
#     @abstractmethod
#     def div(self):
#         pass

#     @abstractmethod
#     def mult(self):
#         pass

# class NasledMath(Math):
#     def __init__(self, a, b):
#         super().__init__(a, b)

#     def add(self):
#         print(self.a + self.b)

#     def sub(self):
#         print(self.a - self.b)

#     def div(self):
#         print(self.a / self.b)

#     def mult(self):
#         print(self.a * self.b)

# nasled = NasledMath(10, 10)
# nasled.add()


# class Car:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model 
#         self.price = price

#     def __str__(self):
#         return f"{self.brand}, {self.model}, {self.price}"

#     def __eq__(self, car):
#         return self.price == car.price

#     def __ne__(self, car):
#         return self.price != car.price

#     def __lt__ (self, car):
#         return self.price < car.price

# bmw = Car("BMW", "IX", 150000)
# lexus = Car("Lexus", "LX570", 150000)
# print(bmw == lexus)
# print(bmw != lexus)
# print(bmw < lexus)
# print(bmw)
# print(lexus)


#1Напишите класс GTA, которая имитирует поведение игры GTA. Там есть много методов, но вы должны сделать основные методы как ходить, атаковать, получать урон и делать деньги. Так конструктор принимает персонажи из игры GTA V (Майкл, Тревор, Франклин), то есть если вы ввели другое имя, то вам он должен выводить "Нету такого персонажа".  И также создайте переменные экземпляра (health 100, money 100, satiety, 100, walk 0)Затем создайте магический метод для того чтоб он возвращает все значения. Создайте метод walk для ходьбы и чтоб когда вызывали метод, в walk добавлялось 1 единица значения. Потом создайте метод attack, которая принимает единицу урона. Если урон между 1 и 20, то он должен выводить "Ваш персонаж атаковал и сделал урон{ваш урон}".  Иначе выводит "Вы не нанесли урон". Затем создайте метод для получения урона(случайное значение).  И также если ваше здоровье закончилась то он должен списать с вашего баланса 10 долларов и также пополнить ваш здоровье на 100 единиц. Сделайте последний метод для заработка денег. То есть когда мы вызываем метод то он должен добавлять 100 долларов в наш баланс. Теперь создайте экземпляр класса и вызовите все методы которые у нас присутствуют. 

#2Создайте журнал с оценками для класса из пяти человек. (Имена можете взять выдуманные).  В этом журнале должны храниться оценки каждого ученика. Считайте, что у каждого ученика должно быть по 5 оценок (в диапазоне от 1 до 100 баллов). Высчитайте среднее арифметическое значение оценок для каждого ученика. Сохраните и выведите в переменную имя и средний балл лучшего ученика.
            
#3Напишите класс Сonstructor, которое имитирует строительство жилого дома. В конструкторе мы передаем сколько этажей мы хотим построить. Затем делаем метод build, который строит наш дом пока мы не дойдем до этажа которую мы хотим построить. И также создайте магический метод __str__, для выведение данных нашего класс


# from statistics import mean

# class Journal:
#     def estimatioт(self, ocenka):
#         self.ocenka = ocenka  
#         {'Denis' : {17, 40, 60, 29, 48}, 'Kolya' : {38, 92, 10, 59, 72}, 'Sasha' : {93, 58, 29, 48, 27}, 'Bektur' : {96, 20, 40, 60, 20}, 'Almaz' : {47, 39, 87, 67, 20}}
#         return(mean(ocenka))


# name = """\xd0\x92 \xd1\x81\xd1\x82\xd1\x80\xd0\xbe\xd0\xba\xd0\xb5 "\xd0\xbf\xd0\xbe\xd0\xbb\xd1\x8f \xd0\xb4\xd0\xbb\xd1\x8f \xd0\xb7\xd0\xb0\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x8b" \xd0\xb7\xd0\xb0\xd0\xba\xd0\xbb\xd1\x8e\xd1\x87\xd0\xb0\xd1\x8e\xd1\x82\xd1\x81\xd1\x8f 
# \xd0\xb2 \xd1\x84\xd0\xb8\xd0\xb3\xd1\x83\xd1\x80\xd0\xbd\xd1\x8b\xd0\xb5 \xd1\x81\xd0\xba\xd0\xbe\xd0\xb1\xd0\xba\xd0\xb8\xc2\xa0{}. \xd0\x92\xd1\x81\xd0\xb5, \xd1\x87\xd1\x82\xd0\xbe \xd0\xbd\xd0\xb5 \xd0\xb7\xd0\xb0\xd0\xba\xd0\xbb\xd1\x8e\xd1\x87\xd0\xb5\xd0\xbd\xd0\xbe \xd0\xb2 \xd1\x81\xd0\xba\xd0\xbe\xd0\xb1\xd0\xba\xd0\xb8, \xd0\xb2\xd0\xbe\xd1\x81\xd0\xbf\xd1\x80\xd0\xb8\xd0\xbd\xd0\xb8\xd0\xbc\xd0\xb0\xd0\xb5\xd1\x82\xd1\x81\xd1\x8f \xd0\xba\xd0\xb0\xd0\xba \xd0\xbe\xd0\xb1\xd1\x8b\xd1\x87\xd0\xbd\xd1\x8b\xd0\xb9 \xd1\x82\xd0\xb5\xd0\xba\xd1\x81\xd1\x82, \xd0\xba\xd0\xbe\xd1\x82\xd0\xbe\xd1\x80\xd1\x8b\xd0\xb5 \xd0\xba\xd0\xbe\xd0\xbf\xd0\xb8\xd1\x80\xd1\x83\xd0\xb5\xd1\x82\xd1\x81\xd1\x8f \xd0\xb2 \xd0\xbd\xd0\xb5\xd0\xb8\xd0\xb7\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xbe\xd0\xbc \xd0\xb2\xd0\xb8\xd0\xb4\xd0\xb5. \xd0\xa7\xd1\x82\xd0\xbe\xd0\xb1\xd1\x8b \xd0\xbf\xd0\xb5\xd1\x80\xd0\xb5\xd0\xb4\xd0\xb0\xd1\x82\xd1\x8c \xd0\xb2 \xd1\x82\xd0\xb5\xd0\xba\xd1\x81\xd1\x82\xd0\xb5 \xd1\x81\xd0\xb8\xd0\xbc\xd0\xb2\xd0\xbe\xd0\xbb\xd1\x8b \xd1\x84\xd0\xb8\xd0\xb3\xd1\x83\xd1\x80\xd0\xbd\xd1\x8b\xd1\x85 \xd1\x81\xd0\xba\xd0\xbe\xd0\xb1\xd0\xbe\xd0\xba, \xd0\xb8\xd1\x85 \xd0\xb4\xd1\x83\xd0\xb1\xd0\xbb\xd0\xb8\xd1\x80\xd1\x83\xd1\x8e\xd1\x82:\xc2\xa0{{\xc2\xa0\xd0\xb8\xc2\xa0}}.\xd0\x9f\xd0\xbe\xd0\xbb\xd1\x8f \xd0\xb4\xd0\xbb\xd1\x8f \xd0\xb7\xd0\xb0\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x8b \xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0\xd1\x82\xd0\xb8\xd1\x80\xd1\x83\xd1\x8e\xd1\x82\xd1\x81\xd1\x8f \xd1\x81\xd0\xbb\xd0\xb5\xd0\xb4\xd1\x83\xd1\x8e\xd1\x89\xd0\xb8\xd0\xbc \xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb7\xd0\xbe\xd0\xbc"""
# print(name.decode("UTF-8"))

# frzn = frozenset({1, 2, 3})
# print(frzn)


# names = [1, 2, 3, 4, 5, 6]
# numbers = []
# print(names)
# for i  in names :
#     numbers.append(i + 1)
    
# print(numbers)



# import time
# from random import randint


# for i in range(1,1000):
#     print('')


# class OldCar:
#     def __init__(self, brand, model, year):
#         self.brand = brand 
#         self.model = model 
#         self.year = year 

#     def info(self):
#         return f"{self.brand}, {self.model}, {self.year}"

#     def engine(self):
#         return f"Мотор"

#     def carcase(self):
#         return f"Кузов"
    
#     def weels(self):
#         return f"Колеса"
    
#     def mehanic_gear_box(self):
#         return f"Механическая коробка передачи"

# old_car = OldCar("Ford", "Shelby", 1917)
# print(old_car.engine())
# print(old_car.carcase())
# print(old_car.weels())
# print(old_car.mehanic_gear_box())
# print(old_car.airbag())




# class NewCar(OldCar):
#     def __init__(self, brand, model, year, odometer, color):
#         super().__init__(brand, model, year)
#         self.odometer = odometer
#         self.color = color 

#     def airbag(self):
#         return f"Подушка безопасности"

#     def autopilot(self):
#         return f"Авто пилот"

# new_car = NewCar("Ford", "Mustang", 2020, 0, "White")
# print(new_car.engine())
# print(new_car.carcase())
# print(new_car.weels())
# print(new_car.mehanic_gear_box())
# print(new_car.airbag())
# print(new_car.autopilot())

# class Cat: 
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def make_sound(self):
#         return "Meoww"

# class Dog:
#     def __init__(self, name, age ):
#         self.name = name
#         self.age = age
    
    
#     def make_sound(self):
#         return "Gaaww"


# class Cow: 
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def make_sound(self):
#         return "Muu"



# cat = Cat("Alisa", 20)
# dog = Dog("Alaba", 2)
# cow = Cow("Korova", 10)
# for animal in (cat, dog , cow):
#     print(animal.make_sound())



# import random

# class Phone:
#     def __init__(self, brand, model, year):
#         self.brand = brand 
#         self.model = model 
#         self.year = year 
#         self.__battery = 100
#         self.__status_battery = 100

#     def use_phone(self):
#         if self.__battery <= 0:
#             return "Зарядите телефон"
#         else:
#             random_use = random.randint(1, 20)
#             if self.__battery >= random_use:
#                 self.__battery -= random_use
#                 return f"Вы использовали телефон у вас осталось {self.__battery}"
#         return f"Зарядите телефон"

#     def power_phone(self):
#         if self.__battery >= 0 and self.__battery <= 100:
#             self.__battery = 100
#             self.__status_battery -= 2
#             return "Вы зарядили свой телефон"
#         else:
#             return f"У вас достаточно заряда"

#     def __str__(self):
#         return f"{self.brand}, {self.model}, {self.__battery}% заряда, максимальная емкость {self.__status_battery}"

# iphone_13 = Phone("Iphone", "13", "2022")
# print(iphone_13.use_phone())
# print(iphone_13.use_phone())
# print(iphone_13.use_phone())
# print(iphone_13.use_phone())
# print(iphone_13.use_phone())
# print(iphone_13.use_phone())
# print(iphone_13.use_phone())
# print(iphone_13.use_phone())
# print(iphone_13.use_phone())
# print(iphone_13.use_phone())
# print(iphone_13.use_phone())
# print(iphone_13)
# print(iphone_13.power_phone())
# print(iphone_13)
# # iphone_13.__battery = 10000
# # iphone_13.__battery = 1000
# print(iphone_13)

# iphone_13._Phone__status_battery = 2000
# print(iphone_13)
# print(iphone_13._Phone__battery)

# class A:
#     def say_hello(self):
#         return "Hello"

# class B:
#     def  say_bye(self):
#         return f"Bye"

# class C(A , B):
#     def dinner(self):
#         return  f"Dinner"

# class D(C):
#     pass

# d = D()
# print(d.say_bye())
# print(d.say_hello())
# print(d.dinner())


# class Dad:
#     def drive(self):
#         return f"Иметь машину"

# class Mom:
#     def cooking(self):
#         return f"Готовить блюдо"

# class Son(Dad):
#     pass

# class Daughter(Mom):
#     pass


# daughter = Daughter()
# print(daughter.cooking())



# from abc import ABC, abstractmethod

# class Math(ABC):
#     def __init__(self, a, b):
#         self.a = a 
#         self.b = b 

#     @abstractmethod
#     def add(self):
#         pass 

#     @abstractmethod
#     def sub(self):
#         pass 

#     @abstractmethod
#     def div(self):
#         pass 

#     @abstractmethod
#     def mult(self):
#         pass

# class MathSub(Math):
#     def __init__(self, a, b):
#         super().__init__(a, b)

#     def add(self):
#         return self.a + self.b 

#     def sub(self):
#         return self.a - self.b 
        
#     def div(self):
#         return self.a / self.b

#     def mult(self):
#         return self.a * self.b 

# math_sub = MathSub(10, 10)
# print(math_sub.add())
# print(math_sub.sub())
# print(math_sub.div())
# print(math_sub.mult())


# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname

#     @property
#     def full_name(self):
#         return self.name + ' ' + self.surname

 
#     @full_name.setter
#     def full_name(self, new):
#         self.name, self.surname = new.split(' ')
        