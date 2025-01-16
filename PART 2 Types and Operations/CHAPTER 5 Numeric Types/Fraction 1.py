from fractions import Fraction
x=Fraction(1,3)
print('x',x)
y=Fraction(5,6)
print('y',y)
add=x+y
print('add',add)
sub=x-y
print('sub',sub)
mul=x*y
print('mul',mul)

a1=Fraction('0.25')
print('a1',a1)
a2=Fraction('1.25')
print('a2',a2)
add=a1+a2
print('add',add)

a3=Fraction(1,10)+Fraction(1,10)+Fraction(1,10)-Fraction(3,10)
print('a3',a3)

from decimal import Decimal
a4=Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3')
print('a4',a4)
