def merge(ls,st,m,end):
 i=st
 j=m+1
 temp=[]
 while i<=m and j<=end:
    if ls[i]<ls[j]:
        temp.append(ls[i])
    i+=1
 else:
        temp.append(ls[j])
        j+=1
 while i<=m:
     temp.append(ls[i])
     i+=1
 while j<=end:
     temp.append(ls[j])
     j+=1
 k=0 
 for i in range(st,end+1):
    ls[i]=temp[k]
    k+=1
 
def merge_sort(ls,st,end):
 if st<end:
     m=st+(end-st)//2
 merge_sort(ls,st,m)
 merge_sort(ls,m+1,end)
 merge(ls,st,m,end)
ls=[23,54,65,45,3,45,4,345,45,2]
merge_sort(ls,0,len(ls)-1)
print(ls)