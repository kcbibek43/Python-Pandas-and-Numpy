n = int(input("Enter a row "))
for i in range(1,n+1):
    x = 0
    for j in range(1,i+1):
        if(i%2 == 1):
            if(j%2==1):
                print(x+1,end=" ")
            else:
                print(x,end=" ")
        else:
            if(j%2==0):
                print(x+1,end=" ")
            else:
                print(x,end=" ")
    print("")