def sum(n):
    if(n == 0):
        return 0
    x = n%10
    n//=10
    return sum(n) + x
n = int(input("Enter a number "))
x = sum(n)
print("The sum of digit of " , n , " is ", x)