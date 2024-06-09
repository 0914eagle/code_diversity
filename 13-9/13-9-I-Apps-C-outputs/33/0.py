
def count_distinct_times(n, m):
    # Initialize a set to store the distinct times
    distinct_times = set()

    # Iterate over each hour
    for hour in range(n):
        # Iterate over each minute
        for minute in range(m):
            # Convert the hour and minute to base 7
            hour_base7 = convert_to_base7(hour)
            minute_base7 = convert_to_base7(minute)

            # Check if the hour and minute are distinct
            if hour_base7 != minute_base7:
                # Add the time to the set of distinct times
                distinct_times.add((hour, minute))

    # Return the number of distinct times
    return len(distinct_times)

# Convert a decimal number to base 7
def convert_to_base7(num):
    # Initialize the base 7 representation of the number
    base7_rep = ""

    # While the number is greater than 0
    while num > 0:
        # Get the remainder of the number when divided by 7
        remainder = num % 7

        # Add the remainder to the base 7 representation
        base7_rep = str(remainder) + base7_rep

        # Update the number
        num //= 7

    # Return the base 7 representation of the number
    return base7_rep

