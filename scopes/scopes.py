# Области видимости и пространство имен 

# built-in (Встроенная) - print, len, max, int 
# Global (Глобальная)
# Enclosed (не локальнаяб nonlocal)
# local(локадьная область видимости)

# def print_list(some_list):
#     for element in some_list:
#         print(element)
# element = 'q'
# print_list([1, 2, 3, 4, 5,])

# a = 10 
# print 
# def hello():
#     a = 'Hello world'
#     print(a)
# hello()
# print(a)

# x = 'global'
# print(x) #global

# def enclosed():
#     x = 'enclosed'
#     def local():
#         x = 'local'
#         print(x) #local
#     print(x) #enclosed
#     local()
#     print(x) #enclosed

# enclosed()
# print(x)


# num = 10
# def func():
#     def inner_func():
#         print(num)
#     inner_func()

# func()


# var = 100

# def increment():
#     var = var + 1 # Try to update a global variable(using -> var += 1)

# increment()

# global -> позволяет менять значения глобальной переменной находясь в локальной
# области видимости  

# nonlocal - > позволяет менять значения не локальной переменной находясь в локальной области видимости

# var = 100
# def increment():
#     global var
#     var += 1
# print(var)
# increment()
# increment()
# increment()
# increment()
# print(var)


# def counter():
#     num = 0
#     def incrementer():
#         nonlocal num
#         num += 1
#         return num
#     return incrementer

# c = counter()
# print(c) #<function counter.<locals>.incrementer at 0x7f36f7c86040>
# print(c()) #1
# print(c()) #2
# print(c()) #3
# c = counter()
# print(c())

# print(dir(__builtins__))


# print(abs(-15)) #Стандартный вызов встроенной функции
# abs = 15 #Переопределяю встроенной имя fbs в глобальной области 
# print(abs)

# a = [[1, 2, 3], [3, 4, 5]]
# 1
# sums = []
# for i in a:
#     sums.append(sum(i))
# print(sums)
# print(max(sums))
# 2
# res = max([sum(x) for x in a])
# print(res)

# alice = [13, 15, 38]
# john = [5, 15, 50]
# # res = {'Alice': 1, 'John' : 1}
# # rec = {'Alice' : None, 'John' : None}
# def won(a, j):
#     score_a = 0
#     score_j = 0
#     for i in range(0, len(a)):
#         if a[i] > j[i]:
#             score_a += 1
#         elif j[i] > a[i]:
#             score_j += 1
#         else:
#             pass
#     return {'Alece' : score_a, 'John' : score_j}

# print(won(alice, john))


# a = 'Pythooon'
# c = {key: a.count(key) for key in a}
# print(c)





    # for i in alice, john:
    #     if alice > john: 
    #         i = 'Alice' + 1
    #     elif john > alice:
    #          = 'John' + 1
