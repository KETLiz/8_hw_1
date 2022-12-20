import json

def delete():
    user_for_del = input('Введите имя контакта, которое хотите удалить: ')
    with open('8_hw/data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        minimal = 0
        for txt in data:
            if txt['Name'] == user_for_del:
                data.pop(minimal)
            else:
                None
            minimal = minimal + 1
        with open('8_hw/data.json', 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, indent=2)