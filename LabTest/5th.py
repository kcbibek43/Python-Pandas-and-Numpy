def C(n,r):
    p = float(input("Enter the principle for intreset: "))
    x = (1+r/100)
    pw = x ** n
    ans = pw*p - p
    return ans
n = int(input("Enter number of years: "))
r = float(input("Enter intrest rate: "))
ans = C(n,r)
print("The compound intrest is: ",ans)