def power(n,e):
    res=1
    for i in range(e):
        res *= n
    return res
x = int(input("Enter a number "))
y = int(input("Enter power "))
print(power(x,y))