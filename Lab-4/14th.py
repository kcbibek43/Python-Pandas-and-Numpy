str = "This is reversing a string"
l = len(str)-1
s = ""
while l>=0:
    s += str[l]
    l-=1
print("The string in reverse is ",s)