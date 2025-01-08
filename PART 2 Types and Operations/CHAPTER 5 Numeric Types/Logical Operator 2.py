#logical operator: and,or, not
a1=8
a2=2
a3=7
a4=3
print('a1',a1,'a2',a2,'a3',a3,'a4',a4)
res=a1<a2 and a3<=a4
print('res',res)
res=a1>a2 or a4<=a1
print('res',res)
res=not a1<a4
print('res',res)
res=a1>a2 or a3<a1
print('res',res)
res=a4>=a2 and a3<=a4
print('res',res)
res=a3>a4 and a1<a2
print('res',res)
res=a1>a3 and a4<a3
print('res',res)
res=a1>a3 and a4>a2
print('res',res)
