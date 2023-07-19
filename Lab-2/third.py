salary = float(input("Enter the salary "))
gender = input("Enter your gender (F/M): ")
bonus = 0;
if salary<20000:
    bonus += salary * 0.05
    if gender == 'M':
        bonus += salary * 0.05
    else:
        bonus += salary * 0.1
else:
    if gender == 'M':
        bonus += salary * 0.05
    else:
        bonus += salary * 0.1
print("Bonus of the employee: ",bonus)
print("Final Salary of the employee: " , salary+bonus)

