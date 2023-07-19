print("Enter the numbers until -1: ")
pos = 0
neg = 0
while True:
    x = int(input())
    if x==-1:
        break
    if x>0:
        pos+=1
    elif x<0:
        neg+=1
print("The number of positive is ",pos ," and negative is ",neg)
