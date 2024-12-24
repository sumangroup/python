a={1,2,3,4,5}
b={1,2,6,7}
e={10,11,12}
f={8,9,15}
g={16,19,21}
print("a=",a,"b=",b)
union=a | b | e | f | g
print("union:",union)
intersection= a & b
print('intersection:',intersection)
set_difference=a-b;
print('set_difference:',set_difference)
set_difference=b-a;
print('set_difference:',set_difference)
set_symmetric_difference=a ^ b
print('set_symmetric_difference:',set_symmetric_difference)

c={1,2,3,4,5}
d={1,3,5}
Superset=c>d
print('Superset',Superset)
subset=d<c
print('subset',subset)
