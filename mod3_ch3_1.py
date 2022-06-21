from math import sqrt
def area(a, b, c):
    p = int((a + b + c)/2)
    s = int(sqrt(p*(p-a)*(p-b)*(p-c)))
    return (s)
    pass
a =int(input('Введите первую сторону треугольника: '))
b =int(input('Введите вторую сторону треугольника: '))
c =int(input('Введите третью сторону треугольника: '))
print(area(a,b,c))
