income = float(input("Enter your annual income: "))
tax = 0;
if income<=300000:
    tax = 0
elif income>300000 and income<=500000:
    tax = income*0.05
elif income>500000 and income<=1000000:
    tax = income*0.2
else:
    tax = income*0.3
print("Your tax amount is " , tax)