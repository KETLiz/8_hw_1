
def write(name, surname, job, number, mail):
    with open('8_hw/file.txt', 'a', encoding='utf-8') as data:
        data.write(f'Имя: {name}, Фамилия: {surname}, Должность: {job}, Номер телефона: {number}, e-mail: {mail}\n')
        
def get_base():
    with open('8_hw/file.txt', 'r', encoding='utf-8') as data:
        return data.readlines()        