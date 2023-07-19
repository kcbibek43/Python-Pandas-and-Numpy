def gdc(n1,n2):
    if(n2 == 0):
        return n1
    else:
        return gdc(n2,n1%n2)
n1 = int(input("Enter a number "))
n2 = int(input("Enter a another number "))
x = gdc(n1,n2)
print("The gcd of two number is ",n1 , " and ", n2, " is ",x)