hr1 = int(input("Enter 1st hr "))
min1 = int(input("Enter 1st min "))
sec1 = int(input("Enter 1st sec "))
hr2 = int(input("Enter 2nd hr "))
min2 = int(input("Enter 2nd min "))
sec2 = int(input("Enter 2nd sec "))
sec = (sec1+sec2)%60
carry = (sec1+sec2)//60
min = (min1+min2+carry)%60
carry1 = (min1+min2+carry)//60
hr = (hr1+hr2+carry1)%24
day = (hr1+hr2+carry1)//24
if(day==0):
    print("The sum time is ", hr ,"hrs",min,"min",sec,"sec")
else:
    print("The sum time is ",day," day", hr ,"hrs",min,"min",sec,"sec")