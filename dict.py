dic1 = {1:'aa', 2: 'bb', 3: 'cc'}
print(dic1)
print(dic1[1])
print(dic1.get(2))
print(dic1.items())
print(dic1.keys())
print(dic1.values())

for i in dic1.keys():
    print('%s -> %s' % (i, dic1[i]))