# dict() -  словарь -> это упорядочкенный коллекция элементов (python 3.7 -> ovdered)
# каждый элемент в словаре содержится в паре ключ: значение
# Ключи должны быть уникальными и быть неизменяемый типом данным(str, int, tuple ect)
# Тогда как значениями могут выступать любые типы данных.


# thisdic = {
#     'brand' : 'Ford',
#     'model' : 'mustang',
#     'year' : 1965
# }
# print(thisdic)
# print(type(thisdic))


# Hash tables, фссщциативный массив, dictionary, object(js) == dictionary(py)

# some_tuple = {1, 2, 3}
# print(type(some_tuple))

# some_dict = {}
# print(type(some_dict))
# key_value = {'key' : 'value', 'key' : 'value1'}
# print(type(key_value))
# dict_created = dict()
# print(type(dict_created))

# dict_ = dict((('key', 'value', ), ('key2', 'value2')))
# print(dict_)
# print(type(dict_))

#----------------------------------------------------------




# user_info = {
#     'first_name' : 'John',
#     'last name' : 'Snow',
#     'age' : 24,
#     'email' : 'Johnsno221@gmail.com',
#     'role' : [1, 2, 3],
#     #[1,2,3]: 'list' #Error
#     # 'first_name' : 'Raychel'
# }
# print(user_info['first_name'])
# print(user_info.get('age'))
# print(dir(user_info))

# print(user_info.items())
# for items in user_info.items():
#     print(user_key)

# print(user_info.keys()) # before changes

# user_info['height'] = 187

# print(user_info.keys()) # after changes
# print(user_info)
# for key in user_info.keys():
#     print(key)


# for value in user_info.values():
#     print(value)

# pop() - Удаляет элемент по определенному ключу
# popitem() - Удаляет по последнию пару в словаре


# print(user_info)
# user_info.pop('email', 'role')
# user_info.popitem()

# print(user_info)


# setdefault(key, [default, value]) - Работает так же как и метод get(), но если такого ключа не существует, 
# то оно созждаст новую значению.

# 1 значения примененияб получения значния
# dict_ = {'name' : 'John', 'age' : '24'}
# result = dict_.setdefault('age')
# print(result)

# 2 способ применения, добавления пары
# dict_ = {'name' : 'John', 'age' : '24'}
# result = dict_.setdefault('address', 'Toktogula str.')
# print(dict_)

 
# print(user_info)
# user_info.update({'name' : 'Raychel'})
# user_info.update({'height' : 199})
# print(user_info)

# ----------------------------------------

# roles = {
#     0: 'Admin',
#     1: 'Moderator',
#     2: 'Vendor',
#     3: 'Customer',
#     4: 'Guest'
# }

# users = [
#     {
#         'id': 1,
#         'name': 'John',
#         'role': roles[0],

#     },
#     {
#         'id': 2,
#         'name': 'Raychel',
#         'role': roles[1]
#     }
# ]
# product = {
#     'id':1,
#     'title':'Samsung Galaxy S20',
#     'desciption':'Lorem Ipsum',
#     'price':1000
# }
# # print(users)


# user_id = int(input('Enter id: '))
# if users[user_id]['role'] == roles[0]:
#     product['discription'] = input('Enter new description of product: ')
# else:
#     raise Exception('You have no right')
# print(product)

