#Tuples
t1=()
print('t1',t1,len(t1))
t2=(1,2,3)
print('t2',t2,len(t2))
t3=1,2,3
print('t3',t3,len(t3))
t4=(1,2,3,('raju','aryan'))
print('t4',t4,len(t4))
t5=tuple(['raju'])
print('t5',t5,len(t5))

t6=(
   1,2,3,['java','python']
    )
print('t6',t6,len(t6))
print('t6[0]',t6[0])
print('t6[1]',t6[1])
print('t6[2]',t6[2])
print('t6[3]',t6[3])
print('t6[3][1]',t6[3][1])
print('t6[1:3]',t6[1:3])
print('t6[1:]',t6[1:])
print('t6[:2]',t6[:2])

for x in t6:
    print(x)

t7=(0,2,4,3,1,5,6,1)
print('t7',t7,len(t7))
count=t7.count(10)
print('count',count)
index=t7.index(1)
print('index',index)
