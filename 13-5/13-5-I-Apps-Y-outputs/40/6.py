
def get_next_larger_number(x):
    # Convert the input to a list of individual digits
    digits = [int(digit) for digit in str(x)]
    
    # Sort the digits in descending order
    digits.sort(reverse=True)
    
    # Check if the digits are already in descending order
    if digits == sorted(digits, reverse=True):
        # If they are, return 0 as there is no larger number with the same digits
        return 0
    
    # If the digits are not in descending order, find the first pair of adjacent digits that are in descending order
    for i in range(len(digits) - 1):
        if digits[i] > digits[i + 1]:
            # If we find a pair of adjacent digits in descending order, swap them and break the loop
            digits[i], digits[i + 1] = digits[i + 1], digits[i]
            break
    
    # Sort the remaining digits in descending order
    digits[i + 1:] = sorted(digits[i + 1:], reverse=True)
    
    # Convert the list of digits back to an integer and return it
    return int("".join(str(digit) for digit in digits))

def main():
    x = int(input())
    print(get_next_larger_number(x))

if __name__ == "__main__":
    main()

