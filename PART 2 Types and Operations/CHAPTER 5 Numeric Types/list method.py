l1=[]
print('l1',l1,len(l1))

print('append')
l1.append(1)
print('l1',l1,len(l1))
l1.append(1)
l1.append("rohan")
l1.append(1)
print('l1',l1,len(l1))
l1.append(10)
print('l1',l1,len(l1))
l1.append(100)
l1.append(10)
print('l1',l1,len(l1))
print('-'*80)

print('count')
a=l1.count(10)
print('a',a)
print('-'*80)

print('index')
b=l1.index(10,5)
print('b',b)
print('-'*80)

print('insert')
print('l1',l1,len(l1))
l1.insert(4,"raju")
print('l1',l1,len(l1))
print('-'*80)

print('pop')
print('l1',l1,len(l1))
c=l1.pop()
print('l1',l1,len(l1))
c=l1.pop(4)
print('l1',l1,len(l1),c)
print('-'*80)

print('remove')
print('l1',l1,len(l1))
l1.remove(1)
print('l1',l1,len(l1))
l1.remove(10)
print('l1',l1,len(l1))
print('-'*80)

print('reverse')
print('l1',l1,len(l1))
print('l1[1]',l1[1])
l1.reverse()
print('l1',l1,len(l1))
print('l1[1]',l1[1])
print('-'*80)


l2=[10,7,8,2,1,63,52]
print('l2',l2,len(l2))
l2.sort()
print('l2',l2,len(l2))
l2.sort(reverse=True)
print('l2',l2,len(l2))
print('-'*80)

l3=[15,23,65]
print('l3',l3,len(l3))
l3.extend([1,2,3])
print('l3',l3,len(l3))
l3.extend((56,78,96))
print('l3',l3,len(l3))
l3.extend("raju")
print('l3',l3,len(l3))
l3.extend({5,6,8,9})
print('l3',l3,len(l3))
print('-'*80)

l4={1,2,3,5,6}
for x in l4:
    print(x)

for x in "raju":
    print(x)
    

