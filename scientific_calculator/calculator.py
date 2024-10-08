import math


class Calculator:

    @staticmethod
    def _add(x: float, y: float) -> float:
        print(f"{x} + {y} =")
        return x + y

    @staticmethod
    def _subtract(x: float, y: float) -> float:
        print(f"{x} - {y} =")
        return x - y

    @staticmethod
    def _multiply(x: float, y: float) -> float:
        print(f"{x} * {y} =")
        return round(x * y, 6)

    @staticmethod
    def _divide(x: float, y: float) -> float:
        print(f"{x} / {y} =")
        return round(x / y, 6)

    @staticmethod
    def _modulo(x: float, y: float) -> float:
        print(f"{x} % {y} =")
        return round(x % y, 6)

    @staticmethod
    def _raise_to_power(x: float, y: float) -> float:
        print(f"{x} ** {y} =")
        return round(x ** y, 6)

    @staticmethod
    def _square_root(x: float) -> float:
        print(f"√{x} =")
        return round(math.sqrt(x), 6)

    @staticmethod
    def _logarithm(x: float, y: float) -> float:
        if y == 10:
            print(f"log({x}) =")
        else:
            print(f"log base {y} ({x}) =")
        return round(math.log(x, y), 6)

    @staticmethod
    def _sine(x: float, in_degrees: bool = False) -> float:
        if in_degrees:
            print(f"sin({x}°) =")
            x = math.radians(x)
        else:
            print(f"sin({x} radians) =")
        return round(math.sin(x), 6)

    @staticmethod
    def _cosine(x: float, in_degrees: bool = False) -> float:
        if in_degrees:
            print(f"cos({x}°) =")
            x = math.radians(x)
        else:
            print(f"cosine({x} radians) =")
        return round(math.cos(x), 6)

    @staticmethod
    def _tangent(x: float, in_degrees: bool = False) -> float:
        if in_degrees:
            print(f"tan({x}°) =")
            x = math.radians(x)
        else:
            print(f"tan({x} radians) =")
        return round(math.tan(x), 6)

    @staticmethod
    def _ask_two_values():
        while True:
            try:
                value1 = float(input("First value: "))
                value2 = float(input("Second value: "))
            except ValueError:
                print("Must be a valid number.")
                continue
            return value1, value2

    @staticmethod
    def _ask_log_values():
        while True:
            try:
                value = float(input("Value: "))
                if value <= 0:
                    print("Logarithm is undefined for non-positive numbers.")
                    continue

                base = input("Provide base input (if empty, default base of 10 will be used): ")
                if base == "":
                    base = 10
                else:
                    base = float(base)
                    if base <= 0:
                        print("Logarithm base must be greater than 0.")
                        continue
                return value, base

            except ValueError:
                print("Must be a valid number.")
                continue

    @staticmethod
    def _ask_sqrt_value():
        while True:
            try:
                value = float(input("Value: "))
                if value < 0:
                    print("Square root is undefined for negative numbers.")
                    continue
                return value
            except ValueError:
                print("Must be a valid number.")
                continue

    @staticmethod
    def _ask_trig_values():
        while True:
            try:
                input_type = input("Input 'D' if providing degrees, 'R' if radians: ")
                if input_type.lower() not in ["d", "r"]:
                    print("Invalid input.")
                    continue
                degrees = True if input_type == "d" else False
                angle = float(input("Input value: "))
                return angle, degrees
            except ValueError:
                print("Must be a valid number.")
                continue

    def _get_user_input_values(self, operation: str):
        value1 = None
        value2 = None

        if 0 <= int(operation) <= 5:
            value1, value2 = self._ask_two_values()
        elif operation == "6":
            value1 = self._ask_sqrt_value()
        elif operation == "7":
            value1, value2 = self._ask_log_values()
        elif 7 < int(operation):
            value1, value2 = self._ask_trig_values()
        return value1, value2

    def handle_operations(self, operation: str):
        result = None
        while True:
            value1, value2 = self._get_user_input_values(operation)
            if value2 == 0 and operation in ["3", "4"]:
                print("Cannot divide by zero.")
                continue
            break

        operations = {
            "0": self._add,
            "1": self._subtract,
            "2": self._multiply,
            "3": self._divide,
            "4": self._modulo,
            "5": self._raise_to_power,
            "6": self._square_root,
            "7": self._logarithm,
            "8": self._sine,
            "9": self._cosine,
            "10": self._tangent,
        }

        operation_func = operations.get(operation)
        if operation_func:
            if operation == "6":
                result = operation_func(value1)
            else:
                result = operation_func(value1, value2)
        else:
            print("Invalid operation.")
        return result
