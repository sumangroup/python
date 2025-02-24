num=int(input("Enter the number: "))
num1=num
rev=0

while num!=0:
    r=num%10
    rev=rev+r**3
    num=num//10

print(rev)
if num1==rev:
    print(num1,"this is armstrong  number")
else:
    print(num1,"this is not armstrong  number")
