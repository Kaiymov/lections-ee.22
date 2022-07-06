from itertools import product
import json
import random
from secrets import choice

FILE_PATH = 'data.json'

def get_data(): 
    with open(FILE_PATH) as file:
        return json.load(file)

def list_of_products():
    data = get_data()
    return data

def retrieve_product(): 
    data = get_data()
    id = int(input('vvedite id producta: '))
    product = list(filter(lambda x: x['id'] == id, data))
    return product[0]

def get_id():
     with open('id.txt', 'r') as file:
        id = int(file.read())
         
        id += 1
     with open('id.txt', 'w') as file :
      file.write(str(id))
      return id 
def create_product():
    data = get_data()
    product = {
        'id': get_id(), 
        'title': input('vvedite nazvanie producta: '),
        'price': int(input('vvedite price producta: ')),
        'description': input('vvedite opisanye: ')
    }
    data.append(product)

    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)
    result = {'msg': 'created', 'product': product}
    return result

def update_product():
    data = get_data()
    flag = False
    id = int(input('Enter id product: '))
    product = list(filter(lambda x: x['id'] == id, data))

    if not product:
        return {'msg': 'invalid id! Product does not exist!'}
    print(product)

    index = data.index(product[0])
    choice = input('What do change?(title-1, price-2, description-3): ')

    if choice == '1':
        data[index]['title'] = input('Enter new name product: ')
        flag = True
    elif choice == '2':
        data[index]['price'] = float(input('Enter new price: '))
        flag = True
    elif choice == '3':
        data[index]['description'] = input('Enter new description: ')
        flag = True
    else:
        print('INvalod choice to update!!!')
      

    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)
    
    if flag:
        return {'msg': 'Updated', 'product': data[index]}
    else:
        return {'msg': 'Not Updated!!!'}

def delete_product():
    data = get_data()
    id = int(input('Enter id product: '))
    product = list(filter(lambda x: x['id' == id, data]))

    if not product:
        return {'msg': 'invalid id! Product does not exist!'}

    index = data.index(product[0])
    deleted = data.pop(index)

    json.dump(data, open(FILE_PATH, 'w'))

    return {'msg': 'Deleted', 'product': deleted}



