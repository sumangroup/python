set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
print('set1',set1)
print('set2',set2)
#set1.difference_update(set2)
#set1.intersection_update(set2)
#set1.symmetric_difference_update(set2)
set1.update(set2)
print('set1',set1)
print('set2',set2)
