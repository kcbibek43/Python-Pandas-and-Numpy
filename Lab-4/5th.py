def binarySearch(l,n,x):
    low = 0
    high = n-1
    while low<high:
        mid = (low+high)//2
        if(l[mid]==x):
            return mid
        elif(l[mid]<x):
            low = mid + 1
        else:
            high = mid - 1
    return -1
l = [1,2,3,4,89,2,34,12,45]
l.sort()
y = binarySearch(l,9,34)
if(y==-1):
    print("The element in not in the list ")
else:
    print("The element is found at index ",y)
