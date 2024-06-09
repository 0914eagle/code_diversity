
def solve(k, a):
    # Initialize variables
    days = [0, 0, 0, 0, 0, 0, 0]
    total_days = 0
    current_day = 0
    classes_taken = 0

    # Loop through the input array
    for i in range(len(a)):
        # If the current day has classes, add it to the days array
        if a[i] == 1:
            days[i] += 1

    # Loop through the days array
    for i in range(len(days)):
        # If the current day has classes and we have not reached the required number of classes, add it to the total days
        if days[i] > 0 and classes_taken < k:
            total_days += 1
            classes_taken += 1
        # If the current day has classes and we have reached the required number of classes, break the loop
        elif days[i] > 0 and classes_taken == k:
            break
        # If the current day does not have classes, move to the next day
        else:
            current_day = (current_day + 1) % 7

    # Return the total days
    return total_days

