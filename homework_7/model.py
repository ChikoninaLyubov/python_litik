phone_book = []
path = 'homework_7/phone_book.txt'

def get_phone_book():
    global phone_book
    return phone_book

def open_file():
    global phone_book
    global path
    with open(path,'r',encoding='UTF-8') as data:
        file = data.readlines()
    for contact in file:
        phone_book.append(contact.strip().split(';'))

def save_file():
    global phone_book
    global path
    pb_str = []
    for contact in phone_book:
        pb_str.append(';'.join(contact))
    with open(path,'w',encoding='UTF-8') as data:
        data.write('\n'. join(pb_str))

def add_new_contact(new_contakt: list):   
    global phone_book
    phone_book.append(new_contakt)

def search_contact(find:str):
    global phone_book
    result = []
    for contact in phone_book:
        for field in contact:
            if find in field:
                result.append(contact)
                break
    return result   

def delete_contact(delete_contact: str):
    phone_book = search_contact()
    if delete_contact == '':
        return
    else:
        phone_book.pop(int(delete_contact))
        with open(path, 'w', encoding='utf8') as data:
            data.write('')
        for i in phone_book:
            search_contact(i)
                  
