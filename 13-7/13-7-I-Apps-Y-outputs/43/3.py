
def guess_numbers(x1, x2, x3, x4):
    # Initialize a list to store the guessed numbers
    numbers = []

    # Check if x1 + x2 = x3
    if x1 + x2 == x3:
        numbers.append(x1)
        numbers.append(x2)

    # Check if x1 + x3 = x2
    if x1 + x3 == x2:
        numbers.append(x1)
        numbers.append(x3)

    # Check if x2 + x3 = x1
    if x2 + x3 == x1:
        numbers.append(x2)
        numbers.append(x3)

    # Check if x1 + x2 + x3 = x4
    if x1 + x2 + x3 == x4:
        numbers.append(x1)
        numbers.append(x2)
        numbers.append(x3)

    # Return the guessed numbers in any order
    return numbers

