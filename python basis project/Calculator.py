# write a pyhton program to create basics calculator 

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

choise = input("\n\nEnter the opperator and avalible operator are\nfor subtraction (-) \nfor Additon (+) \nfor Multiplecation (*) \nfor Division (/)\n\t\t")


if choise == "+":
    print("the Additon of given two number is " + str(num1+num2))
    
if choise == "-":
    print(f"the subtraction of given two number is {num1-num2}")
    
if choise == "*":
    print(f"the multiplectin of given two number is {num1*num2} ")
    
if choise == "/":
    print(f"the division of given two number is {num1/-num2} ")
