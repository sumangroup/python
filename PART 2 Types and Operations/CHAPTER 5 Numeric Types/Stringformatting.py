#String formatting
s1='My name is %s. My age is %d. My salary is %f'%("Raju Ramchandra Mane",32,25000.23)
print('s1',s1)
print("-"*80)

name="Raju Ramchandra Mane"
age=32
salary=25000.23
s1='My name is %s. My age is %d. My salary is %f'% (name,age,salary)
print('s1',s1)
print("-"*80)

s1='My name is %s. My age is %s. My salary is %s'%("Raju Ramchandra Mane",32,25000.23)
print('s1',s1)
print("-"*80)


s1="Raju"
res='%s' %(s1)
print(res)
res='%6s' %(s1)
print(res)
res='%6s' %(s1)
print(res,len(res))
res='%+6s' %(s1)
print(res,len(res))
res='%06s' %(s1)
print(res,len(res))
res='%010s' %(s1)
print(res,len(res))
res='% 10s' %(s1)
print(res,len(res))
print('-'*80)


x=1.23456745
print('x',x)
s1='%f'%(x)
print('s1',s1)
x=12345.6745
print('x',x)
s1='%e'%(x)
print('s1',s1)
x=1.23456745
print('x',x)
s1='%e'%(x)
print('s1',s1)

z='%E'%(1562356854565125.5458545263)
print('z',z)
s1='%g'%(x)
print('s1',s1)
x=0.00000123
print('x',x)
s1='%g'%(x)
print('s1',s1)
print('-'*80)
x=1.23456745
print('x',x)
s1='%f'%(x)
print('s1',s1)
s1='%6.3f'%(x)
print('s1',s1)


