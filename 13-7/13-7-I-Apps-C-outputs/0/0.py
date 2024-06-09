
def find_number(m, n, p, q):
    # Initialize a list to store the digits of the number
    digits = []
    # Loop through each digit of the number
    for i in range(m):
        # If the digit is not in the first n digits, add it to the list
        if i >= n:
            digits.append(i)
    # Join the digits into a string
    number = "".join(str(digit) for digit in digits)
    # Multiply the number by q and add p
    result = int(number) * q + p
    # If the result is a valid m-digit number, return it
    if len(str(result)) == m:
        return result
    # Otherwise, return the string "IMPOSSIBLE"
    else:
        return "IMPOSSIBLE"

