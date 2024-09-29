def perform_operation(num1: float, num2: float, operation: str) -> float:
    """
        Perform a mathematical operation on two numbers.

        Args:
            num1 (float): The first number.
            num2 (float): The second number.
            operation (str): The operation to perform. Supported operations are 'add', 'subtract', 'multiply', and 'divide'.

        Returns:
            float: The result of the operation.

        Raises:
            ValueError: If an unsupported operation is passed.
            ZeroDivisionError: If division by zero is attempted.
    """

    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y if y != 0 else (_ for _ in ()).throw(ZeroDivisionError("Cannot divide by zero"))
    }

    if operation in operations:
        return operations[operation](num1, num2)
    else:
        raise ValueError(f"Unsupported operation '{operation}'. Supported operations are: {', '.join(operations.keys())}")

