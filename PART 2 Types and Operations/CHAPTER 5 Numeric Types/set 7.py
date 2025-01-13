# set
s1={1,2,3,4,2,4}
s2={1,4,6,7}
print('s1',s1,'s2',s2)
union=s1 | s2
print('union',union)
intersection= s1 & s2
print('intersection',intersection)
difference_s1=s1 - s2
print('difference_s1',difference_s1)
difference_s2=s2 - s1
print('difference_s2',difference_s2)
symmetric_difference= s1 ^ s2
print('symmetric_difference',symmetric_difference)

s3={}
print('s3',type(s3))
s4=set()
print('set',s4)
