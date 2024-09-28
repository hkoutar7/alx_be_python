def get_task_details() -> tuple[str, str, str]:
    """
        Prompts the user for task details: task description, priority, and if it's time-bound.

        Returns:
            tuple: task (str), priority (str), time_bound (str)
    """

    task = input("Enter your task: ")

    priority = input("Priority (high/medium/low): ").lower()
    while priority not in {"high", "medium", "low"}:
        print("Invalid priority. Please enter 'high', 'medium', or 'low'.")
        priority = input("Priority (high/medium/low): ").lower()

    time_bound = input("Is it time-bound? (yes/no): ").lower()
    while time_bound not in {"yes", "no"}:
        print("Invalid input. Please enter 'yes' or 'no'.")
        time_bound = input("Is it time-bound? (yes/no): ").lower()

    return task, priority, time_bound


def generate_reminder(task: str, priority: str, time_bound: str) -> str:
    """
        Generates a reminder based on task priority and whether it's time-bound.

        Args:
            task (str): The task description.
            priority (str): The task's priority level ('high', 'medium', or 'low').
            time_bound (str): Indicates if the task is time-sensitive ('yes' or 'no').

        Returns:
            str: A customized reminder message for the user.
    """

    reminder = f"'{task}' is a {priority} priority task."

    match priority:
        case "high":
            reminder += " It's critical to focus on this task."
        case "medium":
            reminder += " You should aim to complete it soon."
        case "low":
            reminder += " Consider completing it when you have free time."

    if time_bound == "yes":
        reminder += " This task requires immediate attention today!"
    
    return reminder


def main():
    """
        Main function that handles task input and reminder generation.
    """

    task, priority, time_bound = get_task_details()

    reminder = generate_reminder(task, priority, time_bound)
    print(f"\nReminder: {reminder}")


if __name__ == "__main__":
    main()
