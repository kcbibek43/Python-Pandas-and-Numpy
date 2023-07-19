import math
def prime(a):
    for i in range (2,int(math.sqrt(a))+1):
        if(a%i == 0):
            return False
    return True
n = int(input("Enter a number "))
for i in range (2,int(n/2)):
    if(n%i==0):
        if(prime(i)):
            print(i)