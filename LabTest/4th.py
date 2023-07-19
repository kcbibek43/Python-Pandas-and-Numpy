print("Select your Choice ")
print("1.Add")
print("5.Subtract ")
print("3.Multiply")
print("4.Division")
while (True):
    c = int(input("Enter your choice: "))
    if(c>4 or c<1):
        print("Invalid Input")
    else:
        num1 = float(input("Enter 1st number "))
        num2 = float(input("Enter 2nd number "))
        if(c==1):
            print(num1+num2)
        elif (c==2):
            print(num1-num2)
        elif (c==3):
            print(num1*num2)
        elif (c==4):
            print(num1/num2)
    next = input("Do you want to continue (Yes/No): ")
    if(next == "No"):
        break
