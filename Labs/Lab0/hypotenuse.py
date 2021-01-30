import math


def CalculateHypotenuse(a: float, b: float) -> float:
    """
    Calculate the hypotenuse length of a triangle.

    :precondition: a and b must be positive numbers
    :postcondition: calculates the length of hypotenuse
    :param a: the first side length of a triangle
    :param b: the second side length of a triangle
    :return: the length of the hypotenuse as a float
    """
    return math.sqrt(a ** 2 + b ** 2)


def main():
    side1 = float(input("Enter the first side"))
    side2 = float(input("Enter the second side"))
    try:
        print(CalculateHypotenuse(side1, side2))
    except Exception as e:
        print("Bad input!")


if __name__ == '__main__':
    main()
