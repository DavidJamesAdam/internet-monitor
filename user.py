from datetime import datetime, timedelta


def user_interval():
    """Asks the user what interval of time they'd like to test for.

    Returns:
        int: User specified time in minutes (int)

    Raises
        ValueError: If time is not specified in the corrent format.
    """
    while True:
        try:
            s = int(input("Enter an interval to test for (minutes): "))
            return s * 60
        except ValueError:
            print("Invalid input. Please enter a valid number of minutes: ")


def runtime():
    """Asks the user how long they'd like the test to run for. 

    Returns:
        int: User specified runtime in minutes.

    Raises
        ValueError: If time is not specified in the corrent format.
    """
    while True:
        try:
            r = int(
                input("How long do you want the test to run for (minutes): "))
            return datetime.now() + timedelta(minutes=(r))
        except ValueError:
            print("Invalid input. Please enter a valid number of minutes: ")
