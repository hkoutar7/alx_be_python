
def calculate(num1: float, num2: float, operation: str) -> str:
    """
        Perform a mathematical operation between two numbers.

        Args:
            num1 (float): The first number.
            num2 (float): The second number.
            operation (str): The operation to perform ("+", "-", "*", "/").

        Returns:
            str: The result of the operation, or an error message in case of invalid operation or division by zero.
    """

    match operation:
        case "+":
            return f"The result is {num1 + num2}."
        case "-":
            return f"The result is {num1 - num2}."
        case "*":
            return f"The result is {num1 * num2}."
        case "/":
            if num2 == 0:
                return "Cannot divide by zero."
            return f"The result is {num1 / num2}."
        case _:
            return "Invalid operation selected. Please choose from +, -, *, /."


def main():
    """
        Main function to prompt user input and perform the requested calculation.
    """

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    operation = input("Choose the operation (+, -, *, /): ")

    result = calculate(num1, num2, operation)
    print(result)


if __name__ == "__main__":
    main()
