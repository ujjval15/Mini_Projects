# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result

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



