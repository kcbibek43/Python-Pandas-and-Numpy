ls = [1,2,3,4,5,6,7]
l = len(ls)
lst = []
for i in range (l-1,0,-1):
    if(i%2==1):
        lst.append(ls[i])
print(lst)
