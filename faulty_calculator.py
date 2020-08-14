# Exercise 2 - Faulty Calculator
# This program should take operator  and the two numbers as input from the user and then return the result
# There is some condition in which if user enter some value then it will print wrong answer

def faulty_calculator():
    while(True):
        operator=input("Enter the Type of Operation, Available Operations: *,/,+ : ")
        value1 = int(input("Enter the value1: "))
        value2 = int(input("Enter the value2: "))

        if operator == '*':
            if value1 == 45 and value2 == 3:
                print(f"Multiplication of {value1} and {value2} is {555}")
            else:
                print(f"Multiplication of {value1} and {value2} is {(value1)*(value2)}")
        elif operator == "/":
            if value1 == 56 and value2 == 6:
                print(f"Division of {value1} and {value2} is {4}")
            else:
                print(f"Division of {value1} and {value2} is {(value1)/(value2)}")
        elif operator == "+":
            if value1 == 56 and value2 == 9:
                print(f"Addition of {value1} and {value2} is {77}")
            else:
               print(f"Addition of {value1} and {value2} is {(value1)+(value2)}")
        inp = input("Do you want to continue calculating? If yes type 'Y' else type 'N' \n")
        if inp.capitalize() == 'Y':
            continue
        else:
            break

faulty_calculator()



