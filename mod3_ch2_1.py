m = [1,4,1,66,'hello','a',5,'hello']
L = []
O = []
for i in m:
    if i not in L:
        L.append(i)
    else:
        O.append(i)
print(O)
