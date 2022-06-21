data = []
a = input('Введите первое число: ')
data.append(a)
b = input('Введите второе число: ')
data.append(b)
c = input('Введите третье число: ')
data.append(c)

first = max(data)
data.remove(first)

second = max(data)
data.remove(second)

third = max(data)
data.remove(third)

print(f'Максимальное число из ваших чисел состовляет {first}{second}{third}')