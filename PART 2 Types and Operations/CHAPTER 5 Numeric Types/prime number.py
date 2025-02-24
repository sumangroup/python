num=int(input("Enter the number : "))
count=0
i=1
while i<=num:
    if num%i==0:
        count=count+1

    i=i+1

if count==2:
    print("This number is prime number")
else:
    print("This number is not prime number")
