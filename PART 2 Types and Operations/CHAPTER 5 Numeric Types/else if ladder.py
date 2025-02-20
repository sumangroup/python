marks1=int(input('Enter the marks1: '))
marks2=int(input('Enter the marks2: '))
marks3=int(input('Enter the marks3: '))
marks4=int(input('Enter the marks4: '))
marks5=int(input('Enter the marks5: '))
total=marks1+marks2+marks3+marks4+marks5
print('total',total)
per=total/500*100
print('per',per)

# if else ladder
if per>=85:
    print('A+')
elif per>=75:
    print('A')
elif per>=65:
    print('B+')
elif per>=55:
    print('B')
elif per>=45:
    print('C')
elif per>=35:
    print('D')
else:
    print('F')
