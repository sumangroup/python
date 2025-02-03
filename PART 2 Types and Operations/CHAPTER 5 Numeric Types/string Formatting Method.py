#Formatting Method
s1='My name is {0},age is {1}, salary is {2} and my no. is {3} and my edu..{4}'
s2=s1.format('Raju Ramchandra Mane',32,25000,9833395327,'M.sc')
print('s2',s2)

s3='{age},{salary},{name},{phone}'
s4=s3.format(name='Raju',phone=9833395327,age=32,salary=25000)
print('s4',s4)

s5='{age},{0},{salary},{1}'
s6=s5.format('Raju Ramchandra Mane',9833395327,salary=25000,age=32)
print('s6',s6)
