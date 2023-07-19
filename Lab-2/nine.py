by = int(input("Enter a binary  number "))
dec = 0
i = 0
while(by>0):
    x = by%10
    by //= 10
    if(x==1):
        dec += 2**i
    i+=1
print(dec," is the number in decimal")
