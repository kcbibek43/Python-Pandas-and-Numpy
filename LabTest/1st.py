n = int(input("Enter a 7 digit no: "))
t = True
for i in range (1,8):
    if(t):
        print(n%10," ")
        t = False
    else:
        t = True
    n//=10