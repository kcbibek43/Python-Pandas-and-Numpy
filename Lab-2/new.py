st = "BIBEK"
length = len(st)
cnt = 0
for i in range(length):
    cnt+=1
    print(st[i])
if(cnt%2==0):
    print("Even")
else:
    print("Odd")
print(cnt)