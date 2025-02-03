# list
l1=[1,2,3,4,5,6,7,8,9]
print('l1',l1,len(l1))

l2=[101,'Raju Mane',32,25000.23,
    ['java','python','c','c++',['java 1.23','java 1.27',['1.27.1','1.23.5']]]]
print('l2',l2,len(l2))
print('l2[0]',l2[0])
print('l2[1]',l2[1])
print('l2[2]',l2[2])
print('l2[3]',l2[3])
print('l2[4]',l2[4])
print('l2[4][2]',l2[4][2])
print('l2[4][4][1]',l2[4][4][1])
print('l2[4][4][2][1]',l2[4][4][2][1])


l3=[
    101,
    {
        'name':'Raju Mane',
        'age':32,
        'salary':25000,
        'skill':['java','python','c','c++']
        }
    ]
print('l3',l3,len(l3))
print('l3[0]',l3[0])
print('l3[1]',l3[1])
print('l3[1][key]',l3[1]['name'])
print('l3[1][age]',l3[1]['age'])
print('l3[1][salary]',l3[1]['salary'])
print('l3[1][skill]',l3[1]['skill'])
print('l3[1][skill][3]',l3[1]['skill'][3])

l4=[
    101,
    {
        'name':'Raju Mane',
        'age':32,
        'salary':25000,
        'skill':['java','python','c','c++',(1.23,1.27)]
        }
    ]
print('l4[1][skill][4][1]',l4[1]['skill'][4][1])







