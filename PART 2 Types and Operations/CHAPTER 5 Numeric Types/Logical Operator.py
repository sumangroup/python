''' This program cover the Logical operators '''
# Logical operators: and, or and not
a1=12
a2=20
a3=15.23
a4=16
print('a1=',a1,'a2=',a2,'a3=',a3,'a4=',a4)
res1=a1<a3 and a2==a4
print('a1<a3 and a2==a4',res1)
res2=a1==a3 or a2==a4
print('a1<a3 or a2==a4',res2)
res3=not a1!=a3
print('a1>a3',res3)
res4=a1==a2>a4!=a2
print('a1==a2>a4!=a2',res4)

res5=a1+a2/a3 >= a4%a3*a2 and a1//a4*a2+a3-a2 != a2*a3-a2
print('a1+a2/a3>=a4%a3*a2 and a1//a4*a2+a3-a2',res5)
res6=a1+a3/a4 > a3//a2 or a2/a4-a2 == a3+a1
print('a1+a3/a4 > a3//a2 or a2/a4-a2 == a3+a1',res6)
res7=not a1+a3/a4 > a3//a2 or a2/a4-a2 == a3+a1
print('not a1+a3/a4 > a3//a2 or a2/a4-a2 == a3+a1',res7)
