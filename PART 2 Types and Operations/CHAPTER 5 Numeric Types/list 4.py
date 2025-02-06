l1= ['spam', 'Spam', 'SPAM!']
print('l1',l1,len(l1))
l1[0:2]=['rohan','arya']
print('l1',l1,len(l1))
print('-'*80)

l2=[1,2,3]
print('l2',l2,len(l2))
l2[1:2]=['aryan','raju']
print('l2',l2,len(l2))
l2[1:1]=['rasika','rohan']
print('l2',l2,len(l2))
print('-'*80)

l3=[1,2,3]
print('l3',l3,len(l3))
l3[1:2]=[4,5]
print('l3',l3,len(l3))
l3[1:1] = [6, 7]
print('l3',l3,len(l3))
l3[1:3]=[]
print('l3',l3,len(l3))
l3[:]=[]
print('l3',l3,len(l3))
print('-'*80)



l4=[1]
print('l4',l4,len(l4))



