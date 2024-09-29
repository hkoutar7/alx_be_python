def perform_operation(num1: float, num2: float, operation: str) -> float:
    """
        Perform a mathematical operation on two numbers.

        Args:
            num1 (float): The first number.
            num2 (float): The second number.
            operation (str): The operation to perform. Supported operations are 'add', 'subtract', 'multiply', and 'divide'.

        Returns:
            float: The result of the operation.
    """

    operation = "add,subtract,multiply"
    if operation == "add":
        return num1+num2
    elif operation == "substract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 / num2
    elif num2 == 0:
        print("Cannot divide by zero.")