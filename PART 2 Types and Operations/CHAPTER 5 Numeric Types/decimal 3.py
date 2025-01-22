from decimal import Decimal,getcontext,localcontext
a1=Decimal('0.1')
a2=Decimal('0.1')
a3=Decimal('0.2')
a4=a1+a2-a3
print('a4',a4)

getcontext().prec=2
a5=Decimal(1)/Decimal(7)
print('a5',a5)

with localcontext() as t:
     t.prec=3
     a5=Decimal(1)/Decimal(7)
     print('a5',a5)

