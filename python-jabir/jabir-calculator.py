import math 
# scientific calculator

# Display the menu to the user for the menu to enter their choice 
while True:

    print("\t\t\t\tjabirs scientific calculator")

    print("\nchoose an Operation from the Menu\n\n1. Adittion\n2.Subtraction\n3. Multiplication\n4. Division\n5. Modulus\n6. Power of a number\n7.Square of a number\n8.Logarithm\n9.Sine\n10. Cosine\n11. Tangent\n")

    # ask the user for their choice 
    operation =  int(input("enter your choice:"))
    # check the user choice and perform the operation that maps to that choice
    # Addtiion 
    if operation == 1:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter The Second Number:"))
        print(f"The sum {num1} and {num2} is {num1 + num2}")
        
        # ask the user to go back to the main menu 
        back = input("go back to the main menu> (Y/N): ")

        if back == "Y":
            continue
        else:
            break 
# 2 subtraction 
    elif operation == 2:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter The Second Number:"))
        print(f"The subtraction of {num1} and {num2} is {num1 - num2}")
        
        # ask the user to go back to the main menu 
        back = input("go back to the main menu> (Y/N): ")

        if back == "Y":
            continue
        else:
            break 
    # multiplication
    elif operation == 3:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter The Second Number:"))
        print(f"The multiplication of {num1} and {num2} is {num1 * num2}")
        
        # ask the user to go back to the main menu 
        back = input("go back to the main menu> (Y/N): ")

        if back == "Y":
            continue
        else:
            break 
     # Divivsion
    elif operation == 4:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter The Second Number:"))
        print(f"The Division of {num1} and {num2} is {num1 / num2}")
        
        # ask the user to go back to the main menu 
        back = input("go back to the main menu> (Y/N): ")

        if back == "Y":
            continue
        else:
            break 
     # Modulus
    elif operation == 5:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter The Second Number:"))
        print(f"The Modulus of {num1} and {num2} is {num1 % num2}")
        
        # ask the user to go back to the main menu 
        back = input("go back to the main menu> (Y/N): ")

        if back == "Y":
            continue
        else:
            break 
    # Power of a number 
    elif operation == 6:
        base = int(input("Enter the base number: "))
        power = int(input("Enter the Exponent/Power: "))
        pow(base, power)
        print(f"The Power of {base} raised to {power} is", pow({base}, {power}))
        # print(f"The Power of {base} raised to {power} is {base ** power}")

        #ask the user to go back to the main menu 
        back = input("go back to the main menu> (Y/N): ")

        if back == "Y":
            continue
        else:
            break 

    # square of a number 
    elif operation == 7:
        num1 = float(input("Enter the first number: "))
        square = 2
        print(f"The Square of {num1}  is {num1 ** square}")
        
        # ask the user to go back to the main menu 
        back = input("go back to the main menu> (Y/N): ")

        if back == "Y":
            continue
        else:
            break 

    # Logarithm
    elif operation == 8:
        Number = float(input("Enter The  Number you wish to find its logarithm to base 2: "))
        print(f"The logarithm of {Number} is {math.log2(Number)}")

        # ask the user to go back to the main menu 
        back = input("go back to the main menu> (Y/N): ")

        if back == "Y":
            continue
        else:
            break 
    # sine
    elif operation == 9:
        num = float(input("Enter the angle in degrees you wish to find its sine: "))
        print(f"The Sine of {num}\u00b0 is {math.sin(math.radians(num))}")

        # ask the user to go back to the main menu 
        back = input("go back to the main menu> (Y/N): ")

        if back == "Y":
            continue
        else:
            break 
    # cosine 
    elif operation == 10:
        num = float(input("enter the angle in degrees you wish to find its cosine: "))
        print(f"The cosine of {num} is {math.cos(math.radians(num))}")

        # ask the user to go back to the main menu 
        back = input("go back to the main menu> (Y/N): ")

        if back == "Y":
            continue
        else:
            break 
    # Tangent 
    elif operation == 11:
        num = float(input("Enter the angle in degrees you wish to find its tangent: "))
        print(f"The Tangnet of {num}\u00b0 is {math.tan(math.radians(num))}")

         # ask the user to go back to the main menu 
        back = input("go back to the main menu> (Y/N): ")

        if back == "Y":
            continue
        else:
            break 
