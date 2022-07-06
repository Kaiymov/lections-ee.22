# JavaScript Object Notation - JSON
# Единый формат хранения и передачи данных междк копьютерами, сервисами, приложениями
# и языками программирования через сеть Интернет.


# <filename>.json


# {
#     'id': 1
# } Это JSON, задача научиться переводить JSON в Python Dict


# !!!
# JS object == {}
# PY dict == {}
# JSON ++ {}

# Процессы Сериализации данных и их Дессериалиция

# Сериализация - (Записывает данные в JSON)это перевод Python Dict в JSON формат (либо сохрвнить все в файл либо сохранять  проксто как текстовый данный)


# dump - метод записывает объект Python в файл в формате JSON 
# dumps - метод записывает объект Python в файл в формате JSON, в строкую


# Дессириализация (Чтенния Данных из JSON) - это процесс перевода из JSONа в Python dict

# load - метод который считывает файл в формате JSON и переводит его в объект Python
# loads - метод который считывает JSON в текстовом формате и переводит его в объекты в Python

# ----------------------------------------------------------------------
# Процесс десериализация
# import json
# from urllib.request import urlopen


# data = urlopen('https://randomuser.me/api/')
# print(type(data))
# # print(data)
# generate_to_dict = json.load(data)
# print(generate_to_dict)
# print(type(generate_to_dict))

# --------------------------------------------

# import json

# with open('downAPI.json', 'r')as file:
#     data = file.read()
#     # print(data)
#     # print(type(data))
#     user = json.loads(data)
#     print(user)
#     print(type(user))

# ----------------------------------------------
# Процесс сериализации 
# import json

# dict_ = {
#     'name': 'John',
#     'last_name': 'Snow',
#     'status': True,
#     'wife': None,
#     'children': False
# }

# with open('new.json', 'w') as file:
#     json.dump(dict_, file)

#-----------------------------------------------------

import json

dict_ = {
    'name': 'John',
    'last_name': 'Snow',
    'status': True,
    'wife': None,
    'children': False
}

string = json.dumps(dict_)
print(string)
print(type(string))