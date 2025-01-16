a1=2.3-2.4
print('a1',a1)

from decimal import Decimal,getcontext,localcontext
a1=Decimal('2.3')
a2=Decimal('2.4')
a3=a1-a2
print('a3',a3)

a1=Decimal(2.3)
a2=Decimal(2.4)
a3=a1-a2
print('a3',a3)

print('getcontext')
getcontext().prec=2
a1=Decimal(2.3)
a2=Decimal(2.4)
a3=a1-a2
print('a3',a3)

a4=Decimal(2.3)+Decimal(2.4)
print('a4',a4)
print()
print('localcontext')
with localcontext() as ctx:
    ctx.prec=4
    a1=Decimal(2.3)
    a2=Decimal(2.4)
    a3=a1-a2
    print('a3',a3)

print('after localcontext')
a1=Decimal(2.3)
a2=Decimal(2.4)
a3=a1-a2
print('a3',a3)
