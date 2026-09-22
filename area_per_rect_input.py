#!/usr/bin/env python3
# Created By: Victor V-C
# Date: 09 22, 2026
# This code will ask for the length and width of a rectangle.
# Then it'll perform a simple calculation, and print the result.


def main():
    # Asks for length of rectagnle
    l = int(input("Enter length of the rectangle (cm): "))

    # Asks for width of rectangle 
    w = int(input("Enter width of the rectangle  (cm): "))

    # Calculates area & perimeter based on l & w
    a = l * w
    p = 2 * (l + w)

    # Displays area & perimeter in Terminal
    print("The area of the rectangle is {}cm²".format(a))
    print("Perimeter of the rectangle  is {}cm".format(p))


if __name__ == "__main__":
    main()
