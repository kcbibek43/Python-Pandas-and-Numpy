lt = []
n = int(input("Enter a range "))
for i in range (0,n):
    i = int(input())
    lt.append(i)
mx = 0
for i in range(0,n):
    if(mx<lt[i]):
        mx = lt[i]
print("The largest number is " , mx)