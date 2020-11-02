from datetime import datetime, timedelta


def user_interval():
    """[summary] add delay

    Returns:
        t_interval
        [type]: [description]
    """
    while True:
        try:
            s = int(input("Enter an interval to test for (minutes): "))
            return s * 60
        except ValueError:
            print("Invalid input. Please enter a valid number of minutes: ")


def runtime():
    """[summary] 

    Returns:
        t_end
        [type]: [description]
    """
    while True:
        try:
            r = int(
                input("How long do you want the test to run for (minutes): "))
            return datetime.now() + timedelta(minutes=(r))
        except ValueError:
            print("Invalid input. Please enter a valid number of minutes: ")
