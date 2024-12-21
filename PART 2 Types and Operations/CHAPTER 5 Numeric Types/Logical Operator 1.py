''' This program cover the Logical operator '''
# logical operators: and ,or ,not
a1=17
a2=23
a3=28.37
a4=12.9
print('a1=',a1,'a2=',a2,'a3=',a3,'a4=',a4)
res1= a1<a2 and a2!=a3
print('a1 and a2',res1)
res2=a3<a4 and a3==a2
print('a3<a4 and a3==a2',res2)
res3=a2>a4 and a2==a1
print('a2>a4 and a2==a1',res3)
res4=a1>=a4 or a2<=a1
print('a1>=a4 or a2<=a1',res4)
res5=a3<=a4 or a2>=a1
print('a3<=a4 or a2>=a1',res5)
res7=a3<=a4
print('a3<=a4',res7)
res8=not a3<=a4
print('not a3<=a4',res8)
res9=not (a3<=a4 or a2>=a1)
print('not a3<=a4 or a2>=a1',res9)
res10=not (a2>a4 and a2==a1)
print('not (a2>a4 and a2==a1)',res10)
