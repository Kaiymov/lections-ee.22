# Операторы сравнения
# Условия операторы
# Логические опраторы 

#  операторы сравнения
# <, >, =, <=, >=, !=

# a = 's'
# print(ord(a))
# v = 'd'
# r = a == v
# print(r)
# print(chr(1081))

#Условные операторы

# if 
# elif
# else

# a = input('как тебя зовут?: ')
# if a == "Умар":
#     print('я знаю тебя')
# elif a == 'Манас':
#     print('вроде знаю')
# else:
#     print('я тебя не знаю')

# # sign
# gmail = input('Введи gmail: ')
# password = input('Введи пароль: ')
# password1 = input('Введи пароль2: ')

# if password != password1:
#     raise Exception('пароль не верный')
# else:
#     print('пароль верный')



# if gmail == 'manas@gmail.com':
#     print('абонент найден')
#     if password == '2005':
#         print('Вы вошли')
#     else:
#         print('пароль не верный')
# else:
#     print('gmail  не верный')

# age = int(input('your age: '))
# if age < 18:
#     print(f'Приходи через {18-age} год')
# else:
#     print('come in')

# Логические операторы
# 1. and -> логический и
# 2. or -> логический или
# 3. not -> лог отрицания

# my_age  = 20
# your_age = 18
# result = (my_age == 20) and (your_age == 18)
# print(result)

# result = my_age < 18 or your_age == 18
# print(result)

# result = not my_age != 20
# print(result)



is_user_google_user = True
is_user_github_user = True
is_user_age_greater_21 = False
user_accounts_coins = 8000

if (is_user_google_user and is_user_github_user) and (is_user_age_greater_21 or user_accounts_coins > 5000):
    print('You can enter thr system mr John Snow')
else:
    print('Sorry, you should have Google and Github accounts!')





