
def solve(k, a):
    # Convert the input array to a binary string
    binary_string = "".join(str(int(i)) for i in a)

    # Initialize the minimum number of days to stay in the capital as the length of the binary string
    min_days = len(binary_string)

    # Iterate over the possible starting positions in the binary string
    for i in range(len(binary_string)):
        # Initialize the number of days spent in the capital as 0
        days = 0

        # Iterate over the characters in the binary string starting from the current position
        for j in range(i, len(binary_string)):
            # If the current character is 1, it means there are classes for guest students on the corresponding day of the week
            if binary_string[j] == "1":
                # Increment the number of days spent in the capital
                days += 1

                # If the number of days spent in the capital is equal to the required number of days, break the loop
                if days == k:
                    break

        # If the number of days spent in the capital is less than the minimum number of days, update the minimum number of days
        if days < min_days:
            min_days = days

    # Return the minimum number of days to stay in the capital
    return min_days

