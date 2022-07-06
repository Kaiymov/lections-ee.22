# list()(списокб массив) - изменяемый, последовательный тип данных,
# который из себя представляет коллекцию каких либо объектов.

# my_list = [1, 'string', False, True, [1, 2, 3]]
# print(my_list)
# print(type(my_list))



# 1. -> list(<Iterable>) 

# my_list = list('hello world')
# print(my_list)

# tuple_ = ('banana', 'apple', 'cherry')
# print(tuple_)
# print(type(tuple_))
# my_list = list(tuple_)
# print(my_list)
# print(type(my_list))

# 2. range() -> возращает последовательность элементов(числа)

# a = list(range(2, 15, 2))
# print(a)

# 3. -> []

# my_list = [1, 34, 2]
# print(type(my_list))
# print(my_list)

# print(dir(list))

# append(element) -> Добавляет  element  в конец списка

# list_ = [1, 2, 3]
# print(list_)
# list_.append(5)
# list_.append([1, 2, 3])
# print(list_)

# extend(element[iterable]) -> расширяет список добавляя element в конце

# list_ = [1, 2, 3]
# list_.extend('hello')
# print(list_)

# insert(<index>, <element>) -> добавляет element  по указанному  index

# list_ = ['string', 2, 3, False]
# list_.insert(1, [1, 2, 3, None])
# list_.insert(2, 1)
# print(list_)
# print(list_[5])
# print(list_[1][3])
# print(list_[2:5])
# print(len(list_))

# index(element, [start], [end]) -> возращает индексы  element

# ls = [1, 2, 3, 33, 4, 5, 5, 7, 23, 'hello']
# print(ls.index(5, 6))

# if 'hello' in ls:
#     print('"hello" have in list: ', ls.index('hello'))
# else:
#     print('not have')

# count(element) ->  Возращает количество вхождений  element в списке

# ls = [1, 2, 4, 3, 2, 4, 4, 4, 4, 4, 3]
# result = ls.count(1)
# print(result)

# remove(element) - удаляет  element, но если такого элемента нет то выводит ошибку

# pop([index]) -  удаляет  и возращает элемент по индексу, но если i  элемент
# не указан, то удаляет последние элементы.

# list_ = [5, 1, 2, 3, 4, 5]
# list_.remove(5)
# list_.remove(5)
# deleted = list_.pop(0)
# d = list_.remove(4)
# print(list_)
# print(deleted)
# print(d)

# sort([reverse = True/False], [key=<>])-> сортирует список. Если в аргуементе передан  reverse=True
# то список будет отсортирован в убывающем порядок

# ls = [5, 0, -4, 2, 10, -22, 44, 11]
# print(ls)
# ls.sort(reverse=True)
# print(ls)

# ls = ['manas' , 'Azim', 'khabib']
# ls.sort(key=len, reverse=True)
# print(ls)

# ls = [1, 'h', 3]
# ls[1] = 's'
# print(ls)
# del ls[-1]
# print(ls)



def get_revers(text: str) -> str:
    """
    return reversed string
    """
    list1 = text.split(' ')
    result = ' '. join(list1[::-1])
    print(result)
    return result

get_revers('Hello world! My name is Manas, last name Kaiymov. Nice to meet you')
