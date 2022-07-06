# def sum_of_args(a: int, b: int, c: int, d: int) -> int:
#     """Return sum of all parameters"""
#     return a + b + c + d

# result = sum_of_args
# print(result)

# print(type(result))
# print(result(1, 322, 2, 21))

# -------------------------------
# Позиционые и имеенованные аргументы

# def printParams(a=None, b=None, c=None):
#     print(a, 'is stored in param a')
#     print(b, 'is stored in param b')
#     print(c, 'is stored in param c')

# printParams(c = 3, a = 1)


# def sum_of_args(a: int, b: int, c: int, d: int) -> int:
#     """Return sum of all parameters"""
#     return a + b + c + d

# print(sum_of_args(1 ,2, 3, 4)) # Позиционные аргументы(arguments)
# print(sum_of_args(a=4, b=3, c=2, d=6)) # Именованные аргументы(Keyword argument)
# print(sum_of_args(5, 10, d=23, c=12))


# -----------------------------------

# оператор *

# a = [1, 2, 3]
# b = [4, 5, 6]
# s = [*a, *b]
# print(s)
# print(*a, end='*\b')

# ----------------------------------
# *args, **kwargs

# def print_scores(student, *args):
#     print(f'Student name: {student}')
#     print(args)
#     print(type(args))
#     for i in args:
#         print(f'Grade: {i}')

# print_scores('John Snow', 100, 90, 80, 70, 88, 83)

# def print_pet_names(owner, **pets):
#     print(f'Owner name: {owner}')
#     # print(pets)
#     # print(type(pets))
#     for pet, name in pets.items():
#         print(f'{pet}: {name}')

# print_pet_names('Manas', dog='Rex', cat='Larry', fish = ['Nemo', 'Dori', 'Alex'], turtle='Leonardo')


# def get_some_data(a, b, *args, **kwargs):
#     print('Settings a and b: ', a, b)
#     print(args[0])
#     print(args[-1])
#     print(kwargs['name'])
#     print('Aргументы: ', args)
#     print('Именованные аргументы: ', kwargs)

# get_some_data(1, 2, 3, 4, 5, lang='Python', name='John Snow', car='Nissan R34')

# -------------------------------------------------------


# def conc_two_string(str1, str2):
#     import random
#     res = random.randint(1, 10)
#     return str1 + str2 + str(res)

# result = conc_two_string('Hello', 'World')



# def generate_password(name, fan):
#     import random
#     random_run = random.randint(100000, 999999)
#     return name + fan + '_' + str(random_run)

# def get_info():
#     name = input('Enter your name: ')
#     fam = input('Enter your last name: ')
#     return generate_password(name, fam)

# result = get_info()
# print(result)

# ------------------------------------------

# def  generate_random_string(len_, lang):
#     import string as s
#     import random
#     random_str = ''.join(
#         random.choice(s.ascii_lowercase + s.digits) for i in range(0, len_))
#     return random_str

# print(generate_random_string(15, 'eng'))

# --------------------------------


from re import sub


def add(num1, num2): return num1 + num2

def subtarct(num1, num2): return num1 - num2

def multiply(num1, num2): return num1 * num2

def divide(num1, num2):
    try:
        num1 / num2
    except ZeroDivisionError:
        return 'na 0 delit nelzya'

def main():
    try:
        num1 = float(input('Enter a number: '))
        num2 = float(input('Enter a number: '))
    except ValueError:
        print('Вы ввели некоректно')
        main()

    operator = input('Введите (*, /, -, +): ')
    result=None

    if operator=='+': result = add(num1, num2)

    elif operator=='-': result=subtarct(num1, num2)

    elif operator=='*': result=multiply(num1, num2)

    elif operator=='/': result=divide(num1, num2)

    else:
        print('Вы ввели некоректный оператор')
    print(result)
    
    question = input('Do you want contiun? (Yes/No): ')
    if question.lower() == 'yes':
        main()
    else:
        print('Thanks for using our calculator, Bye bye!!!')

main()
