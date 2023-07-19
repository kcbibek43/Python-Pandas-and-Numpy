ch = input("Enter a character: ")
x = ord(ch)
if x>=65 and x<=90:
    x+=32
    print("The charater in uppercase is " , chr(x))
else:
    x-=32
    print("The charater in uppercase is " , chr(x))
