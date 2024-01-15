aa=[]
aa.append(1)

aa.append(3)

aa.append(5)

aa.append(7)

aa.append(9)

for i in range(0,100):
    aa.append(i)
print(len(aa))

print(aa[:10])
del(aa[1])
print(aa[:2])

list1=[]
list2=[]
value=1

for i in range(0,3):
    for k in range(0,4) :
        list1.append(value)
        value += 1
    list2.append(list1)
    list1=[]

print(list2)