from Labs.Lab0.hypotenuse import CalculateHypotenuse




def main():

    Add = lambda x, y: x + y
    Subtract = lambda x, y: x - y
    Divide = lambda x, y: f"\ninteger: {x // y}\nremainder:{x % y}\n"
    Multiply = lambda x, y: x * y
    Hypo = lambda x, y: CalculateHypotenuse(x, y)

    while True:

        try:

            user_input = int(input(
                "Please enter:\n\t1 to calculate hypotenuse \n\t2 to Add\n\t3 to Subtract\n\t4 to multiply\n\t5 to divide\n"))

            while user_input not in (1, 2, 3, 4, 5):
                print("Unknown option")
                user_input = int(input("Please enter:\n\t1 to calculate hypotenuse \
                \n\t2 to Add\n\t3 to Subtract\n\t4 to multiply\n\t5 to divide\n"))

            val1 = float(int(input("enter first value")))
            val2 = float(int(input("enter second value")))

            if user_input == 1:
                print(Hypo(val1, val2))
            if user_input == 2:
                print(Add(val1, val2))
            if user_input == 3:
                print(Subtract(val1, val2))
            if user_input == 4:
                print(Multiply(val1, val2))
            if user_input == 5:
                print(Divide(val1, val2))
            else:
                continue
        except Exception as e:
            print("Please only input valid input!")


if __name__ == '__main__':
    main()
