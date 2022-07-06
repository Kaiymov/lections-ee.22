# def <name_of_function>(<a, b> #setting)
#     <body> #некий код, некая логика
#     <return #возвращает что-то>

# <name_of_function>(<5, 6> #аргумент)

# Параметры функции - переменные которые будет принимать наша функция, для того что-бы
# мы смогли работать с данными которые предают в эту функции

# return нужен для того что-бы функция что-то возвращало, и для того что-бы мы могли
# работать с рузультатом действия функции
# return является необязательным оператором (возвращает None - если не указать return)


# ls = []
# result = ls.append(1)

# print(ls)
# print(result)

# result1 = ls.pop()
# print(ls)
# print(result1) 


# from unittest import result

# def sumTwoNums(num1, num2):
#     result = num1 + num2
#     return result

# print(sumTwoNums(5, 5)))


# def isEven(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False

# a = 10
# b = int(input('Enter a number: '))
# print(isEven(a))
# print(isEven(b))
# print(isEven(5))


# def isEven1(num: int) -> bool:
#     """
#     Наша функция проверяет является ли число,
#     типа int, четным
#     """
#     if num % 2 == 0:
#         return True
#     return False

# isEven()
# isEven1()
# dir()


# def get_polindrom(words: list) -> list:
#     """
#     Функция возвращает список из полиндромов
#     """
#     result = []
#     for word in words:
#         if word.lower() == word[::-1].lower():
#             result.append(word)
#     return result

# some_words = ['Manas', 'Ono', 'kazak', 'anna', 'Potato', 'Dovod', 'Tan', 'Ata']
# print(get_polindrom(some_words))


# def func():
#     print('hello world')
# func()

# ----------------------------------
# deault params


# def print_welcome(name: str = 'User') -> str:
#     print(f'Welcome, {name}')
# print_welcome()




# def depozit(money: float, period: int) -> float:
#     """
    
#     """
#     if money < 30000:
#         raise Exception('Сумма должна быть больше 30000 сом')
#     if period < 3:
#         raise Exception('Срок вложения должен больше 3 года')
#     i = 0
#     while i < period:
#         # money + 1.1
#         # money + (money / 100 * 10)
#         money = money + (money*0.1)
#         i += 1 # i + i + 1
#     return money

# money = float(input('Сумма: '))
# period = int(input('Срок: '))

# print(depozit(money, period))


def get_revers(text: str) -> str:
    """
    return reversed string
    """
    list1 = text.split(' ')
    result = ' '. join(list1[::-1])
    print(result)
    return result

get_revers('Hello world! My name is Manas, last name Kaiymov. Nice to meet you')
