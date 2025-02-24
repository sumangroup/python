num=int(input("Enter the number: "))
num1=num
rev=0
while num!=0:
    r=num%10
    rev=rev*10+r
    num=num//10

print(num1," is reverse number is",rev)
if num1==rev:
    print("this number is palindrome")
else:
    print("this is not palindrome")
