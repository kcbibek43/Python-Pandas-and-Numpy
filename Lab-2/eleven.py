import math
x = int(input("Enter a number: "))
end = math.sqrt(x)+1
f = 0
i = 2
while(i<end):
    if(x%i==0):
        f+=1
    i+=1

if(f>=1):
    print(x," is a composite number")
else:
    print(x," is prime number")
