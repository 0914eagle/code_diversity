
def solve(k, a):
    # Initialize variables
    days = [0, 0, 0, 0, 0, 0, 0]
    count = 0
    total_days = 0

    # Convert the input list to a binary list
    for i in range(len(a)):
        if a[i] == 1:
            days[i] = 1

    # Iterate through the binary list and count the number of consecutive days with classes
    for i in range(len(days)):
        if days[i] == 1:
            count += 1
        else:
            if count > 0:
                total_days += count
            count = 0

    # If the last day has classes, add it to the total number of days
    if count > 0:
        total_days += count

    # Return the minimum number of days needed to study k days
    return total_days + k

