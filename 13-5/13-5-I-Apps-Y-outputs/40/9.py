
def get_next_larger_number(x):
    # Convert the input to a list of individual digits
    digits = [int(digit) for digit in str(x)]
    # Sort the digits in descending order
    sorted_digits = sorted(digits, reverse=True)
    # Check if the digits are already in descending order
    if digits == sorted_digits:
        # If they are, return 0 as there is no larger number with the same digits
        return 0
    # If the digits are not in descending order, find the first pair of adjacent digits that are in descending order
    for i in range(len(digits) - 1):
        if digits[i] > digits[i + 1]:
            # Swap the digits and break the loop
            digits[i], digits[i + 1] = digits[i + 1], digits[i]
            break
    # Sort the remaining digits in descending order
    sorted_digits = sorted(digits[i + 1:], reverse=True)
    # Add the sorted digits to the beginning of the list
    digits[i + 1:] = sorted_digits
    # Convert the list back to a number and return it
    return int("".join(str(digit) for digit in digits))

def main():
    x = int(input())
    print(get_next_larger_number(x))

if __name__ == "__main__":
    main()

