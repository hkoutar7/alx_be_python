def generate_multiplication_table(number: int) -> None:
    """
        Prints the multiplication table for a given number from 1 to 10.

        Args:
            number (int): The number for which the multiplication table will be generated.
    """

    for i in range(1, 11):
        result = number * i
        print(f"{number} * {i} = {result}")


def main():
    """
        Main function to prompt user input and display the multiplication table.
    """

    try:
        number = int(input("Enter a number to see its multiplication table: "))
    except ValueError:
        print("Please enter a valid integer.")
        return
    
    generate_multiplication_table(number)



if __name__ == "__main__":
    main()
