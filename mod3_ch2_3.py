data = {'name1': 'id1', 'name2': 'id2', 'name3': 'id3'}
inv_data={}
for key,val in data.items():
    inv_data[val]=key #Таким образом Ключ становится на место значения и наоборот, правда почему-то выводит не одной стракой, а три
    print(inv_data)
