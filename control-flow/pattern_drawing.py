def draw_square_pattern(size: int) -> None:
    """
        Draws a square pattern of asterisks (*) with the given size.

        Args:
            size (int): The length of each side of the square pattern.
    """

    row = 0
    while row < size:
        for _ in range(size):
            print("*", end="")
        print(end="\n")
        row += 1


def main():
    """
        Main function to prompt user input and draw the pattern.
    """

    try:
        size = int(input("Enter the size of the pattern: "))
        if size <= 0:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        return

    draw_square_pattern(size)


if __name__ == "__main__":
    main()
