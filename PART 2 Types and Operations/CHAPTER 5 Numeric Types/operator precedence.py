''' This program cover the operator precedence '''
a1=7.5
a2=-2
a3=3.7
a4=12
a5=8
a6=3.7
print('a1=',a1,'a2=',a2,'a3=',a3,'a4=',a4,'a5=',a5,'a6=',a6)
res1=a1//a2 < a3*a4
print('a1//a2 < a3*a4',res1)
res2=a2+a3-a4//a5 >= a1-a2*a3%a5
print('a2+a3-a4//a5 >= a1-a2*a3%a5',res2)
res3=a4*a5/a2//a1 <= a3*a5*a4%a1 != a2
print('a4*a5/a2//a1 <= a3*a5*a4%a1 != a2',res3)
res4= not  a1//a2 < a3*a4 or  a4*a5/a2//a1 <= a3*a5*a4%a1 != a2
print('a1//a2 < a3*a4 and a2+a3-a4//a5 >= a1-a2*a3%a5',res4)
res5=a1+a2//a4%a6 == a3*a4%a5-a1+a3 and a3*a3 == a5 or a1-a5!=a6
print('a1+a2//a4%a6 == a3*a4%a5-a1+a3 and a3*a3 == a5 or a1-a5!=a6',res5)
res6=not a1*a2/a5//a6 != a4*a5/a6-a2+1 and a2//a3//a5*a6 == a6*a5/a2-a1 or a6*a1<=a5//a6 or a5//a4-a6*a3 <= a5//a6
print('res6',res6)
res7=a4//a5 >=a2  or a2
print('res7',res7)
