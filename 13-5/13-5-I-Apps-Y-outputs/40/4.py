
def get_next_larger_number(x):
    # Convert the input to a list of individual digits
    digits = [int(digit) for digit in str(x)]
    
    # Check if the last digit is the largest digit in the number
    if digits[-1] != max(digits):
        # If not, find the index of the last digit that is smaller than the largest digit
        last_smaller_digit_index = len(digits) - 1 - digits[::-1].index(max(digits))
        
        # Swap the last smaller digit with the largest digit
        digits[last_smaller_digit_index], digits[-1] = digits[-1], digits[last_smaller_digit_index]
        
        # Sort the digits in ascending order
        digits.sort()
        
        # Return the next larger number
        return int("".join(map(str, digits)))
    
    else:
        # If the last digit is the largest digit, find the index of the second-to-last digit that is smaller than the last digit
        second_to_last_smaller_digit_index = len(digits) - 2 - digits[::-1].index(digits[-1])
        
        # Swap the second-to-last smaller digit with the last digit
        digits[second_to_last_smaller_digit_index], digits[-2] = digits[-2], digits[second_to_last_smaller_digit_index]
        
        # Sort the digits in ascending order
        digits.sort()
        
        # Return the next larger number
        return int("".join(map(str, digits)))

def main():
    x = int(input())
    print(get_next_larger_number(x))

if __name__ == '__main__':
    main()

