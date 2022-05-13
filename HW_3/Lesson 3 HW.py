# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
# def div(a, b):
#     try:
#         a, b = int(a), int(b)
#         res = a / b
#     except ValueError:
#         return 'не число'
#     except ZeroDivisionError:
#         return ('Ошибка! Делить на ноль нельзя')
#     return res
#
# a = input('Первое число: ')
# b = input('Второе число: ')
# print(div(a, b))

# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. # Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.
# def info (name, surn, birth, city, email, phone):
#     return f'Name:{name}, Surname:{surn}, Birthday:{birth}, City: {city}, Email: {email}, Phone: {phone}'
# print(info(name = input('Name: '),surn = input('Surname: '), birth = input('Birthday: '), city = input('City: '), email = input('Email: '), phone = input('Phone: ')))

# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.
# 3.1
# def exc_min(a, b, c):
#     li = [a, b, c]
#     try:
#         li.remove(min(li))
#         return sum(li)
#     except TypeError:
#         return 'Not a number'
#
# print(exc_min(22, 11, 12))
# 3.2
# def exc_min(a, b, c):
#     li = [a, b, c]
#     try:
#         res = sum(sorted([a, b, c])[1:])
#         return res
#     except TypeError:
#         return 'Not a number'
#
# print(exc_min(8, 3, 12))


# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора
# **. Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
# 4.1
# def my_pow(x, y):
#       try:
#           x, y = float(x), int(y)
#           res = x ** y
#           return res
#       except TypeError:
#           return 'Not a number'
#
# print(my_pow(2, -1))

# 4.2
# def my_pow2(x, y):
#     try:
#         x, y = float(x), int(y)
#         res = 1
#         for _ in range(abs(y)):
#             res /= x
#         return round(res, 7)
#     except TypeError:
#         return 'Not a number'
#
# num1 = input('x: ')
# num2 = input('y: ')
#
# print(my_pow2(num1, num2))


# 5. Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделённых
# пробелом и снова нажать Enter. Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму
# этих чисел к полученной ранее сумме и после этого завершить программу.

# def sum():
#     res = 0
#     while True:
#         li = input('Введите числа через пробел, для выхода - stop: ').split()
#         for num in li:
#             if num.lower() == 'stop':
#                 return res
#             else:
#                 try:
#                     res += int(num)
#                 except TypeError:
#                     print('Для выхода - stop')
#         print('summa = ', res)
#
# print (sum())

# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

# def int_func():
#     li = input('Введите слова через пробел: ').split()
#     for word in li:
#         lenn = 0
#         for ch in word:
#             if 97 <= ord(ch) <= 122:
#                 lenn += 1
#         if lenn == len(word):
#                  print(word.title())
#         else:
#             print(f'Ошибка: {word} - допустим только нижний регстр')
#
# print(int_func())

# 7. Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Используйте написанную ранее функцию int_func().
# def int_func():
#     li = input('Введите слова через пробел: ').split()
#     for word in li:
#         lenn = 0
#         for ch in word:
#             if 97 <= ord(ch) <= 122:
#                 lenn += 1
#         if lenn == len(word):
#                  print(word.swapcase())
#         else:
#             print(f'Ошибка: {word} - допустим только нижний регистр')
#
# print(int_func())


