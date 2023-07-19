age = int(input("Enter The age of candidate : "))
if age>=18:
    print("You are eligible to vote")
else:
    print("You can vote after " , 18-age , " years")