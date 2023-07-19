base = int(input("Enter a base "))
n = int (input("Enter a number "))
ans = 0
i = 0
while(n!=0):
    x = n%base
    n//=base
    ans = x*(10**i) + ans
    i+=1
print("The converted number to base is ",ans)