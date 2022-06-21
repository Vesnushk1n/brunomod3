from random import randint
n = 5
m = [[randint(0,100) for i in range(n)] for j in range(n)]
m2 = []
m3 = 0
print('5 списков: ', m)
for element in m:
    m2.append(max(element))
m3 = (max(m2))
print(m3)