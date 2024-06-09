
def solve(K):
    # Initialize a list to store the Snuke numbers
    snuke_numbers = []

    # Iterate from 1 to 10^15
    for i in range(1, 10**15):
        # Check if the current number is a Snuke number
        if is_snuke_number(i):
            # Add the number to the list
            snuke_numbers.append(i)

            # If the list has reached the desired size, return it
            if len(snuke_numbers) == K:
                return snuke_numbers

    # If the list is empty, return an empty list
    return []

# Check if a number is a Snuke number
def is_snuke_number(n):
    # Get the sum of the digits in the decimal notation of n
    sum_of_digits = sum(int(digit) for digit in str(n))

    # Check if the current number is a Snuke number
    for i in range(n+1, 10**15):
        if sum_of_digits > sum(int(digit) for digit in str(i)):
            return False

    return True

