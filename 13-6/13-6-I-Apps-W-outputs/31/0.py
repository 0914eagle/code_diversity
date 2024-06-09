
def solve(k, a):
    # Convert the input array to a binary string
    binary_string = "".join(str(x) for x in a)

    # Initialize the variables to keep track of the minimum number of days and the current day
    min_days = k
    current_day = 0

    # Iterate through the binary string
    for i in range(len(binary_string)):
        # If the current day has classes, increase the current day by 1
        if binary_string[i] == "1":
            current_day += 1

        # If the current day is equal to the required number of days, update the minimum number of days
        if current_day == k:
            min_days = min(min_days, i + 1)

    # Return the minimum number of days
    return min_days

