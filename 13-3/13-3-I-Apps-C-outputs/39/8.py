
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
    # Multiply the number by q
    number = int(number) * q
    # Add p to the end of the number
    number = str(number) + str(p)
    # Return the number
    return number

