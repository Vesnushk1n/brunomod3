x = int(input('Введите сумму, которая находится на вашем вкладе: '))
p = int(input('Напишите, под каким процентом находится ваша сумма (не более 20%): '))
if p <= 20:
    y = int(input('Напишите, какую сумму вы желаете иметь, а мы напишем, через сколько вы её получите: '))
    i = 0
    while x < y:
        x *= 1 + p / 100
        x = int(100 * x) / 100
        i += 1
    print('Через', i, 'лет вы получите желаемую сумму')
else:
    print('В нашем банке нет вкладов более, чем на 20%')