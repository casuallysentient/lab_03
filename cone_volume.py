"""
WRITE YOUR FUNCTION DEFINITION BELOW
"""
import math

def print_cone_volume():
    radius = int(input("What is the radius of the cone? Only positive numbers allowed.\n"))
    if radius > 0:
        height = int(input("What is the height of the cone? Only positive numbers allowed.\n"))
        if height > 0:
            volume = float(math.pi * (math.pow(radius, 2)) * (height / 3))
            print("The volume of a cone with a radius of " + str(radius) + " and a height of " + str(height) + " is " + str(volume) + ".")
        else:
            print("The value of the radius and the height must be positive.")
    else:
        print("The value of the radius and the height must be positive.")

"""
WRITE YOUR FUNCTION DEFINITION ABOVE
"""


def main():
    """
    When executed, the function print_cone_volume() will prompt the user for two integer inputs. If either one is negative, an error message will be displayed. If they are both positive, they will be substituted into the volume function and a message will be printed that lists the radius, height, and volume.
    """
    print_cone_volume()

### DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
