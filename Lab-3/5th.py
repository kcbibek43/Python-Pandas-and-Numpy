import math
def prime(a):
    for i in range (2,int(math.sqrt(a))+1):
        if(a%i == 0):
            return True
    return False
n = int(input("Enter a number "))
if(prime(n)):
    print("It is not a prime number")
else:
    print("It is a prime number")