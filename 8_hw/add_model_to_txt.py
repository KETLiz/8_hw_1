def add_to_txt():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    job = input('Ваша должность: ')
    number = input('Номер телефона: ')
    mail = input('Введите e-mail: ')
    data = tuple([name, surname, job, number, mail])
    return data    