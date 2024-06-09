
def solve(k, a):
    # Initialize variables
    days = [0, 0, 0, 0, 0, 0, 0]
    total_days = 0
    current_day = 0
    classes_taken = 0

    # Iterate through the input array
    for i in range(len(a)):
        # If the current day has classes, take the class and increment the total days
        if a[i] == 1:
            days[current_day] += 1
            total_days += 1
            classes_taken += 1

        # If the current day is the last day of the week, move to the next week
        if current_day == 6:
            current_day = -1

        # Increment the current day
        current_day += 1

    # If the number of classes taken is less than the required number of classes, return -1
    if classes_taken < k:
        return -1

    # Return the total number of days spent in the capital
    return total_days

