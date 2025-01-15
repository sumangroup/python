a1=0.1+0.1+0.1-0.3
print('a1',a1)

from decimal import Decimal,getcontext,localcontext
a2=Decimal('0.1')
a3=Decimal('0.1')
a4=Decimal('0.1')
a5=Decimal('0.3')
a6=a2+a3+a4-a5
print('a6',a6)
a7=Decimal('2.3')
a8=Decimal('2.4')
a9=a7-a8
print('a9',a9)
a10=Decimal('0.1')+Decimal('0.10')+Decimal('0.10')-Decimal('0.30')

# this has to think
a11=0.2!=0.200000
print("a11",a11)
a12=0.2==0.200000
print('a12',a12)
a1=0.10+0.1+0.1-0.3
print('a1',a1)
a11=Decimal('0.2')+Decimal('0.23')+Decimal('0.256')
print('a11',a11)

getcontext().prec=3
a13=Decimal(1)
a14=Decimal(7)
a15=a13/a14
print('a15,getcontext',a15)

with localcontext() as ctx:
    ctx.prec=2
    a13=Decimal(1)
    a14=Decimal(7)
    a15=a13/a14
    print('a15,localcontext',a15)

a13=Decimal(2)
a14=Decimal(7)
a15=a13/a14
print('a15,getcontext',a15)

