import json
def register():
    with open('data.json', 'r') as f:
        data = json.loads(f.read())
    login = input('Придумайте логин: ')
    if not login in data.keys():
        passwrd = input('Придумайте пароль: ')
        data[login] = passwrd
        with open('data.json', 'w') as f:
            f.write(json.dumps(data))
    else:
        print('Такой пользователь уже есть')

def login():
    with open('data.json', 'r') as f:
        data = json.loads(f.read())
    login = input('Напишите логин: ')
    if login in data.keys():
        passwrd = input('Напишите пароль: ')
        if(data[login] == passwrd):
            print('вы успешно зашли!')
        else:
            print('Неверный пароль или логин')
    else:
        print('Неверный пароль или логин')

log = input('Вы желаете войти или зарегистрироваться? ')
if log.lower() == 'зарегистрироваться':
    register()
elif log.lower() == 'войти':
    login()