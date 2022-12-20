import json

def create_json():
    json_data = []
    with open('8_hw/data.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(json_data, indent=2))
        
def add_contact():
    id = input('Введите id пользователя: ')
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    phone = input('Введите номер телефона: ')
    job = input('Введите должность: ')
    mail = input('Введите e-mail: ')
    
    
    json_data = {
        "id": id,
        "Name": name,
        "Surname": surname,
        "Phone": phone,
        "Job": job,
        "mail": mail
    }  
    
    with open('8_hw/data.json', encoding='utf-8') as f:
        data = json.load(f)
        data.append(json_data)
    with open('8_hw/data.json', 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=2)
    
    
    # data = json.load(open('8_hw/data.json'))
    # data.append(json_data)
    # with open('8_hw/data.json', 'w') as file:
    #     json.dump(data, file, indent=2)
    
        

    #write_data = {'id': id, 'name': name, 'surname': surname, 'phone': phone, 'job': job, 'mail': mail}
    # with open('8_hw/data.json', 'w', encoding='utf-8') as fp:
    #     json.dump(data, fp)