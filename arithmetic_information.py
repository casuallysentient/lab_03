"""
WRITE YOUR FUNCTION DEFINITION BELOW
"""


def print_arithmetic_information():
    number1 = int(input("What is your first positive number?\n"))
    if number1 > 0:
        number2 = int(input("What is your second positive number?\n"))
        if number2 > 0:
            print("")
            sum = number1 + number2
            print(sum)
            difference = number1 - number2
            print(difference)
            product = number1 * number2
            print(product)
            quotient = number1 // number2
            print(quotient)
            remainder = number1 % number2
            print(remainder)
        else:
            print("Values must be positive.")
    else:
        print("Values must be positive.")


"""
WRITE YOUR FUNCTION DEFINITION ABOVE
"""


def main():
    """
    When this function is executed, print_arithmetic_information() will prompt the user for two positive integers. If the user tries to enter a negative number, they will see an error message saying values must be positive. If both are positive, the system will calculate the sum, difference, product, quotient, and remainder when performing the five main operations and print them line by line.
    """
    print_arithmetic_information()

### DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
