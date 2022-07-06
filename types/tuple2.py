# types = (str, int, float, list, tuple)

# for value in types:
#     # print(value)
#     pass

# print(value, True if '__iter__' in dir(value) else False)


# name_lists = ['Ermek', 'Aidana', 'Tima', 'Bermet', 'Zhanylai']

# for name in name_lists:
#     if name.lower() == 'aidana':
#         continue
#     print('hi ' + name)

# sred = len(name_lists) // 2
# name_lists.insert(sred, 'Ramazan')

# for name in name_lists:
#     if name == 'Ramazan':
#         break
#     print(f"hi {name}")

# a = bool(21)
# while a:
#     if input('enter message: ') in 'war drags black'.split():
#         print('Your block')
#         break

# 1)input(email) 2) Show emails

# from secrets import choice


# DB_EMAIL = []

# while True:
#     print(' 1)Input Email 2)Show db_emails 3) Delete gmail in DB 4)Stop while 5)Rename email')
#     choices = int(input('enter choice: '))
#     if choices == 1:
#         email = input('enter email: ')
#         if email.endswith('@gmail.com'):
#             if email in DB_EMAIL:
#                 print('email have in DB')
#                 continue
#             DB_EMAIL.append(email)
#             continue
#         print('ONLY Gmail')
#     elif choices == 2:
#         print(DB_EMAIL)
#     elif choices == 3:
#         email = input('Enter email: ')
#         if email in DB_EMAIL:
#             DB_EMAIL.pop()
#         else:
#             print('Email not found')
#     elif choices == 4:
#         break
#     elif choices == 5:
#         old_email = input('enter email: ')
#         if old_email in DB_EMAIL:
#             new_email = input('email new email: ')
#             if email.endswith('@gmail.com'):
#                 DB_EMAIL.remove(email)
#                 DB_EMAIL.append(new_email)
#                 print('you changed email')
#             elif new_email:
#                 print('email have in DB')
#     else:
#         print('Error!!!')
    
