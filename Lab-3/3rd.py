def rev(n):
    c = 0
    while (n!=0):
        x = n%10
        n //=10
        c = c*10 + x
    return c
n = int(input("Enter a number "))
x = rev(n)
print("The reverse of " , n , " is ", x)
