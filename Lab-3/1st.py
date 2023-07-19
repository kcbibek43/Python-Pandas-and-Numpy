def fact(n):
    if(n==1):
        return 1
    return fact(n-1) * n
n = int(input("Enter a number "))
x = fact(n)
print("The factorial of " , n , " is ", x)