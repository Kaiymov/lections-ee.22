# Работа с файлами

# Каретка -Указатель

# open(<Way untill your file>)

# file = open('/home/manas/Desktop/ev.22/files/files.py') # Абсолютный файл
# file = open('files.py') # Относительный путь

# print(file)

# Режимы для работы с файлами
# 1. r/r+ (read)
# 2. w/w+ (write)
# 3, a/w+ (append)
# t, b, x


# file = open('text.txt', 'r')
# data = file.read()
# print(data)
# print(type(data))




# file = open('/home/manas/Desktop/ev.22/files/text.txt')
# data = file.readlines()
# print(data)
# file.close()


# file = open('text.txt', 'w+')
# file.write('Hello World!!!\nMy name is Makhachkala\nI am Supra')
# print(file.read())
# file.close()

# file = open('text.txt', 'a')
# file.write('\nGanster is cute')
# file.close()


# file = open('text2.txt', 'a')
# file.close()


# Контекстер менеджер

# with open('text.txt', 'r') as file:
#     data = file.read()
#     print(data)

# write
# writelanes

# ls = ['Hello World', 'My name is MacBook', 'I am 100 years old']
# with open('text.txt', 'w') as file:
#     file.writelines(line + '\n' for line in ls)


# file.tell() -> возвращает индекс где находит каретка(указатель)
# file.seek(<int>) -> перемещает    

from PIL import Image
import pytesseract
import re

def get_imei_codes(list_image):
    list_of_imei = []
    for image in list_images:
        string = pytesseract.image_to_string(image)
        print(string)
        list_of_imei.append(re.findall(r'IME.\d.\s\d+', string))
        print(list_of_imei)

list_images = ['imei.jpg']
get_imei_codes(list_images)