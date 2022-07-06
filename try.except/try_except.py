# Обработка исключений
# Операторы: try ... except

# Error - связанные с кодом
# IndentationError
# SyntaxError
# TabError
# ValueError
# BaseException
# ImportError
# KeyError
# IndexError

# try:
#     print(7/0)
# except ZeroDivisionError:
#     print('')

    # num1 = input('Enter a number: ')
    # print(num1)
    # print('очень важная строчка кода')

    

# import sys


# list_ = [1, 2, 3, 4, 5]
# index = int(input('Enter a index: '))

# try:
#     res = list_[index]
#     print(res)
# except:
#     print(f'oops {sys.exc_info()[0]}, error')

#2 Exception as e
# list_ = [1, 2, 3, 4, 5]
# index = int(input('Enter a index: '))

# try:
#     res = list_[index]
#     print(res)
# except Exception as e:
#     print(f'oops {e.__class__}')


# list_ = [1, 2, 3, 4, 5]

# try:
#     index = int(input('Enter a index: '))
#     res = list_[index]
#     print(res)
# except ZeroDivisionError:
#     print('f1!!!')
# except ValueError:
#     print('f2!!!')
# except TabError:
#     print('f3!!!')

# else in try...except
# finally in try...except
# try
#     <body>
# except:
#     <body>
# else:
#     <body> # Сработает если в операторе try не случится ошибка
# finally:
#     <body> # Сраьотает при любом исходе

# try:
#     num1 = int(input('Enter: '))
#     num2 = int(input('Enter: '))
#     result = num1 / num2
# except ZeroDivisionError:
#     print('На 0 делить нельзя')
# except ValueError:
#     print('invalid symbols')
# else:
#     print(result)
# finally:
#     print('Код закончился')