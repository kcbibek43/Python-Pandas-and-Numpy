def linearSearch(l,n,mx):
    for i in range(0,n):
        if(mx<l[i]):
            mx = l[i]
    return mx
l = [1,2,3,4,89,2,34,12,45]
y = linearSearch(l,9,l[0])
print("The maximum element is ",y)