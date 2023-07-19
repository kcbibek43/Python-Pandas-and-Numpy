str = input("Enter a string ")
c = input("Enter a character ")
l = len(str)
flag = False
for i in range(0,l):
    if(str[i]==c):
        flag = True
if(flag):
    print(c," is present in ",str)
else:
    print("Not present")