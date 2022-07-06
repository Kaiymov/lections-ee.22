# map()
# filter()
# lambda
# enumerate()

# Анонимные функции - lambda(такие же функции только без названия)
# Lambda функции могут принимать сколько угодно аргументов, но всегда возвращают только одно выражения

#-------------------------------
# def sum_args(a, b):
#     result = a + b
#     return result
# def sum_args1(a, b): return a + b

# print(sum_args(1, 2))
# print(sum_args1(23, 2))

# ------------------------------

# sum_arg = lambda a, b: a + b
# print(sum_arg(1, 2))

#----------------------------------

# x = lambda a, b, c: a + b + c
# print(x(12, 33, 12))

#----------------------------------

# def myFunc(n):
#     return lambda a: a * n

# my_doubler = myFunc(2)
# my_triple = myFunc(3)

# print(my_doubler(11))
# print(my_doubler(22))
# print(my_triple(11))
# print(my_triple(22))

# -----------------------------------

# ls = ['man', 'Ivan', 'lak', ' ', '']
# new_list = sorted(ls, key = len)
# print(new_list)

# ---------------------------------------


# map(function, Iterables) -> принимает функцию к каждому элементу последовательности,
# и возвращает  mapobject (итератор) с результатами

# Например, с помощью map можно выполнять преоброзования элементов. Перевести все строкии в верхний регистр:

# list_of_words = ['one', 'two', 'three', 'dict']
# result = list(map(str.upper, list_of_words))
# print(result)

# --------------------------------------

# ls = ['1', '2', '3', '4']
# result = list(map(int, ls))
# print(result)

#-------------------------------------------

# names = ['James', 'Christofer', 'Jannat', 'Bold']
# result = list(map(lambda x: f'Hello mr/mrs {x}', names))
# print(result)

# ------------------------------------------

# nums = [1, 2, 3, 4, 5]
# num2 = [100, 200, 300, 400, 500]

# result = list(map(lambda x, y: x*y, nums, num2))
# print(result)

# ----------------------------------------------

# dict_ = {1 : 1, 2 : 2, 3 : 3, 4 : 4}

# result = dict(map(lambda items: (items[0], str(items[1])), dict_.items()))
# print(result)

# -------------------------------------------------


# filter(function, Iterable) -> применяет ко всем элементам itereble функции который мы передает
# и возвращает filterobject(итератор) с теми объектами, для которых функция вернула True 


# list_of_str = ['one', 'two', 'list', '', '100', '32', 'uzb212']

# result = list(filter(str.isdigit, list_of_str))
# print(result)

#--------------------------------------------------------

# ls = [10, 22, 123, 222, 246, 33]
# result = list(filter(lambda x: x % 2 != 0, ls))
# print(result)

#----------------------------------------------------------

# list_of_words = ['John', 'One', 'data', 'date', 'Manas', 'ev.22', 'cat']
# result = list(filter(lambda x: len(x) >=4, list_of_words))
# print(result)

#-------------------------------------------------------

# enumerate(Iterable)

# ls = ['str1', 'str2', 'str3']
# i = 0
# for x in ls:
#     print(f'element: {x}, index {i}')
#     i += 1

# for i, x in enumerate(ls):
#     print(f'element: {x}, index {i}')

# new_list = list(enumerate(ls))
# print(new_list)



# def countingValleys(steps, path):
#     dolina = 0
#     sea_level = 0
#     for x in path:
#         if x == 'U':
#             sea_level += 1
#             if sea_level == 0:
#                 dolina += 1
#         elif x == 'D':
#             sea_level -= 1
#     return dolina
# print(countingValleys(100, 'DUDUUUUUUUUDUDDUUDUUDDDUUDDDDDUUDUUUUDDDUUUUUUUDDUDUDUUUDDDDUUDDDUDDDDUUDDUDDUUUDUUUDUUDUDUDDDDDDDDD'))

# def foo():
#     var = 'переменная foo'
#     print("переменная в foo: ", var)

#     def bar():
#         var = 'переменная bar'
#         print("переменная в foo: ", var)
    
#     bar()

# foo()

# a = {'Murat' : 24, 'Erjan' : 21, 'Chyngyz' : 24, 'Altynai' : 17, 'Asema' : 16}
# c = [k, v for k, v in a.items() if v > 17]

# print(f'Welcome in night club {c}')

# word = "Python"
# vowels = 0
# consonants = 0
# for i in word:
#     letter = i.lower()
#     if letter == "a" or letter == "e" or\
#        letter == "i" or letter == "o" or\
#        letter == "u" or letter == "y":
#         vowels += 1
#     else:
#         consonants += 1
# print("Vowels %i\nConsonants %i" % (vowels, consonants))


# -------------------------------------------------------

# zip(iterables) -  она соединяет каждый элемент итерируемых элементов между собой в тип данных tuple и возвращает это 

# list1 = [1, 2, 3]
# list2 = [100, 200, 300]

# result = list(zip(list1, list2))
# print(result)

# -------------------------------

# a = [1, 2, 3, 4, 5]
# b = [10, 20, 30, 40]
# c = [100, 200, 300]
# result = list(zip(a, b, c))
# print(result)

# ------------------------------------

# zip для создания словарей

# d_keys = ['hostname', 'location', 'vendor', 'IOS', 'IP']
# d_values = ['Shopokov', 'Lenina 3', 'Fal', '12.3', '192.23.2321.2']
# dict_r1 = dict(zip(d_keys, d_values))
# print(dict_r1)

# --------------------------------------------------------

# d_keys = ['hostname', 'location', 'vendor', 'model', 'IOS', 'IP']
# data = {
#     'r1' : ['Shopokov', 'Lenina 0', 'Fal', '12pro max', '12.3', '192.23.321.0'],
#     'r2' : ['Shopokov1', 'Lenina 1', 'Fal', '12pro max', '12.3', '192.23.321.1'],
#     'sw1' : ['Shopokov2', 'Lenina 3', 'Fal', '12pro max', '12.3', '192.23.321.2'] 
# }

# london_data = {}
# for key in data.values():
#     london_data[key] = dict(zip(d_keys, data[key]))
# print(london_data)

# ---------------------------------------------------------------------

# all и any
# all - > возвращает True, если все элементы объекты истинна(или объекь пустой)

# ls = [False, 12, 'test', True]
# print(all(ls))

#- ------------------------------------------------------------

# ip = '192.232.1.22'
# result = all(i.isdigit() for i in ip.split('.'))
# print(result)

# any -> возвращает  True, если хотя бы один элемент истмнный

# ls = [0, 1, False]
# print(any(ls))

# ---------------------------------------------------


# def ignor_command(command):
#     '''
#     Функция проверяет есть ли в команде слово их списка ignor. True - если есть False - если нет такого слова.
#     '''
#     ignor = ['rm -rf', 'alias', 'reset']

#     for word in ignor:
#         if word in command:
#             return True
#     return False

# # print(ignor_command('sudo rm -rf user'))
# command = 'sudo alias'
# if ignor_command(command):
#     raise Exception('Error')
# print('OK')

# ignore = ['rm -rf', 'alias', 'reset']
# command = 'sudo rm -rf home'
# if any(word in command for word in ignore):
#     raise Exception('Открой глаза!!!')
# print('OK!!!')

# from random import choice, choices
# from string import ascii_letters, digits
# from itertools import repeat

# q_pass = int(input('Введите количество паролей: '))

# print({
#     f(choices(ascii_letters, k = 10), choices(digits, k=5))
#     for f in repeat(lambda x , y: ''.join(set((x + y))), q_pass)
# })

