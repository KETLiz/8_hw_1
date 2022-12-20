import json

def red():
    name = input('Введите имя пользователя, чей номер телефона будем менять: ')
    with open('8_hw/data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        for i in range(0, len(data)):
            if name == data[i]['Name']:
                data[i]['Phone'] = input('Введите новый телефон: ')
    with open('8_hw/data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print('Номер успешно изменён!')