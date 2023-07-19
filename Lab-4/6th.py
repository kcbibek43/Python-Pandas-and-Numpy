def selection(l,n,i):
    min = i
    for j in range(i,n):
        if l[min]>l[j]:
            min = j
    return min
l = [12,8,2,7,9,3,4,8,5]
for i in range (0,9):
    x = selection(l,9,i)
    l[i],l[x] = l[x],l[i]
print (l)
