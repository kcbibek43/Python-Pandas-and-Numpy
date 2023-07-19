num = int(input("Enter a number "))
rev = 0;
while(num>0):
    x = num%10
    rev = rev*10 + x
    num //= 10
print("The number in reverse order is " , rev)
