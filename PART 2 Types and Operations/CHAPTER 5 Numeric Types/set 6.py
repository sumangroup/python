#set
s1=set()
print('s1',s1)
s1.add(10)
print('s1',s1)
s1.add(20)
print('s1',s1)
s1.add(24)
s1.add(32)
s1.add(42)
s1.add(27)
print('s1',s1)
s1.add(27)
print('s1',s1)
s2={10,27,15,4,7,18,45}
print('s2',s2)
s3={10,22,93,19,47}
print('s3',s3)
s4=s1.union(s2,s3)     # union
print('s4',s4)
s5=s1.intersection(s2,s3)   #intersection
print('s5',s5)
s6=s1.difference(s2)     #difference
print('s6',s6)
s7=s1.symmetric_difference(s2)
print('s7',s7)
s8=s1.copy()        #copy
print('s8',s8)
print('s1',s1)
s1.discard(32)
print('s1',s1)
s1.discard(99)
s1.remove(24)
print('s1',s1)
#s1.remove(99)
s1.pop()
print('s1',s1)
s1.pop()
print('s1',s1)
s1.pop()
print('s1',s1)
s1.pop()
print('s1',s1)
#s1.pop()
s1.add(10)
s1.add(20)
s1.add(24)
s1.add(32)
s1.add(42)
s1.add(27)
print('s1',s1)
s9={1,3}
print('s9',s9)
s10={4,5,3}
print('s10',s10)
s11=s9.isdisjoint(s10)
print('s11',s11)
s12={1,2}
s13={1,2,3}
print('s12',s12)
print('s13',s13)
s14=s12.issubset(s13)
print('s14',s14)
s15=s13.issuperset(s12)
print('s15',s15)
print('s1',s1)
print('s2',s2)
s16=s1.difference(s2)
print('s16',s16)
print('s1',s1)
#s1.difference_update(s2)
print('s1',s1)
s17=s1.intersection(s2)
print('s17',s17)
print('s1',s1)
#s1.intersection_update(s2)
print('s1',s1)
s18=s1.symmetric_difference(s2)
print('s18',s18)
print('s1',s1)
#s1.symmetric_difference_update(s2)
print('s1',s1)
s19=s1.union(s2)
print('s19',s19)
s1.update(s2)
print('s1',s1)
print('s2',s2)
