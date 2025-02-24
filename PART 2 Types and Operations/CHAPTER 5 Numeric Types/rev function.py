i=1
while i<=10:
    print(i)
    i=i+1

print('-'*80)

def rev(i):
    if i<=10:
        print(i)
        i=i+1
        rev(i)

rev(1)
   
        
