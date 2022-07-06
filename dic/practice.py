

# list1 = []
# for i in range(0, 100):
#     if i % 2 == 0:
#         list1.append(i**2) 
#     elif i % 2 != 0:
#         list1.append(i)
# print(list1)


import random
from secrets import choice

ls = ['Plov', 'Manty', 'Kuurdak', 'Lagman', 'Dymdama']
p = 0
m = 0
k = 0
l = 0
d = 0
for i in range(0, 10000):
    choice = random.choice(ls)
    print(choice)
    if choice.lower() == 'plov':
        p = p + 1
    elif choice.lower() == 'manty':
        m = m + 1
    elif choice.lower() == 'kuurdak':
        k = k + 1
    elif choice.lower() == 'lagman':
        l = l + 1
    elif choice.lower() == 'dymdama':
        d = d + 1
dict_ = {'Plov' : p, 'Manty' : m, 'Kuurdak' : k, 'Lagman' : l, 'Dymdama' : d}
# print(dict_)
result = sorted(dict_.items(), key=lambda x: x[1])
winner = result[-1]
print(f'Победила блюда {winner[0]}, его очко {winner[1]}') 


# print(f'Plov: {p}, Manty: {m}, Kuurdak: {k}, Lagman: {l}')