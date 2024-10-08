import sys
from scientific_calculator.calculator import Calculator


def run_app():
    while True:
        print(
            """Choose the math operation:\n\n0 - Addition\n1 - Subtraction\n2 - Multiplication\n3 - Division\n4 - Modulo
5 - Raising to a power\n6 - Square root\n7 - Logarithm\n8 - Sine\n9 - Cosine\n10 - Tangent\n\nOr 'Q' to quit."""
        )
        calculator = Calculator()
        operation = input("Your selection from the menu: ")
        if operation.lower() == "q":
            sys.exit()
        elif operation not in [str(x) for x in range(11)]:
            print("Invalid input.")
            continue
        result = calculator.handle_operations(operation)
        print(result)

        while True:
            repeat = input("Do you want to make another calculation? (Y/N) ")
            if repeat.lower() == "y":
                break
            elif repeat.lower() != "n":
                print("Invalid input.")
                continue
            else:
                sys.exit()


if __name__ == "__main__":
    run_app()
