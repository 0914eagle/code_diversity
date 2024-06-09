
def solve(n, m):
    # Initialize a set to store the unique pairs
    unique_pairs = set()

    # Loop through each possible hour
    for hour in range(n):
        # Loop through each possible minute
        for minute in range(m):
            # Convert the hour and minute to base 7
            hour_base7 = convert_to_base7(hour)
            minute_base7 = convert_to_base7(minute)

            # Check if the hour and minute have distinct digits
            if has_distinct_digits(hour_base7) and has_distinct_digits(minute_base7):
                # Add the pair to the set
                unique_pairs.add((hour, minute))

    # Return the length of the set
    return len(unique_pairs)

# Convert a number to base 7
def convert_to_base7(num):
    # Initialize the base 7 representation
    base7 = ""

    # Loop until the number is 0
    while num > 0:
        # Get the remainder
        remainder = num % 7

        # Add the remainder to the base 7 representation
        base7 = str(remainder) + base7

        # Update the number
        num //= 7

    # Return the base 7 representation
    return base7

# Check if a number has distinct digits
def has_distinct_digits(num):
    # Initialize a set to store the digits
    digits = set()

    # Loop through each digit in the number
    for digit in str(num):
        # Add the digit to the set
        digits.add(digit)

    # Return True if the set has the same number of elements as the number of digits
    return len(digits) == len(num)

