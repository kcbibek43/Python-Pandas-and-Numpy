def linearSearch(l,n,x):
    for i in range(0,n):
        if(x==l[i]):
            return i
    return -1
l = [1,2,3,4,89,2,34,12,45]
y = linearSearch(l,9,34)
if(y==-1):
    print("The element in not in the list ")
else:
    print("The element is found at index ",y)
