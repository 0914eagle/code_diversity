
def find_number(m, n, p, q):
    # Initialize a list to store the digits of the number
    digits = []
    # Loop through the range of numbers from 1 to 9
    for i in range(1, 10):
        # Check if the current number is valid
        if is_valid(m, n, p, q, i):
            # If the current number is valid, add it to the list of digits
            digits.append(i)
    # If no valid numbers were found, return "IMPOSSIBLE"
    if not digits:
        return "IMPOSSIBLE"
    # Otherwise, return the smallest valid number
    return int("".join(map(str, digits)))

def is_valid(m, n, p, q, num):
    # Check if the number of digits is valid
    if len(str(num)) != m:
        return False
    # Check if the first n digits can be crossed out
    if str(num)[:n] == "0" * n:
        return False
    # Check if the remaining digits can be multiplied by q to get the original number
    if int(str(num)[n:] + str(p)) % q != 0:
        return False
    # If all conditions are met, the number is valid
    return True

