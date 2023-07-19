lt1 = []
lt2 = []
n = int(input("Enter a range "))
for i in range (0,n):
    x1 = int(input())
    lt1.append(x1)
    x2 = int(input())
    lt2.append(x2)
print("The common element are is ")
for i in range(0,n):
    for j in range(0,n):
        if(lt1[i]==lt2[j]):
            print(lt2[j])