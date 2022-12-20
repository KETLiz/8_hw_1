def choose_mode():
    print('Выберите режим работы приложения: ')
    mode = int(input('1 - добавление контакта\n2 - поиск контакта\n3 - удаление контакта\n4 - редактирование контакта\n'))
    return mode

def contact_to_s():
    return input('Введите контакт:')

def search(result):
    for i in result:
        print(i)