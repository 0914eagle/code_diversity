
def get_closest_handsome_numbers(n):
    # Convert the input number to a list of individual digits
    digits = [int(d) for d in str(n)]
    
    # Initialize the closest handsome numbers as the input number itself
    closest_handsome_numbers = [n]
    
    # Iterate through the digits of the input number
    for i in range(len(digits)):
        # If the current digit is odd, check if the next digit is even
        if digits[i] % 2 == 1 and i + 1 < len(digits) and digits[i + 1] % 2 == 0:
            # If the next digit is even, add the current digit to the list of handsome numbers
            closest_handsome_numbers.append(digits[i])
        # If the current digit is even, check if the previous digit is odd
        elif digits[i] % 2 == 0 and i - 1 >= 0 and digits[i - 1] % 2 == 1:
            # If the previous digit is odd, add the current digit to the list of handsome numbers
            closest_handsome_numbers.append(digits[i])
    
    # Sort the list of handsome numbers in ascending order
    closest_handsome_numbers.sort()
    
    # If there is only one handsome number, return it
    if len(closest_handsome_numbers) == 1:
        return closest_handsome_numbers[0]
    # If there are two handsome numbers, return them in ascending order
    else:
        return " ".join(str(n) for n in closest_handsome_numbers)

def main():
    n = int(input())
    print(get_closest_handsome_numbers(n))

if __name__ == '__main__':
    main()

