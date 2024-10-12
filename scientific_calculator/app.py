import sys
from calculator import Calculator


def run_app():
    calculator = Calculator()

    while True:
        print(calculator.menu)
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
