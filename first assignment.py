operation=eval(input("Select an operation 1. Addition, 2.Subtraction, 3.Multiplication, 4.Division: "))

number_1=eval(input("First number: "))
number_2=eval(input("Second number: "))

if (operation == 1):
    print(number_1 + number_2)
elif(operation == 2):
    print(number_1 - number_2)
elif(operation == 3):
    print(number_1 * number_2)
elif(operation == 4):
    print(number_1 / number_2)
else:
    print ("error")