
def get_largest_multiple_of_90(cards):
    # Initialize a list to store the digits
    digits = []
    # Iterate through the cards and add the digits to the list
    for card in cards:
        digits.append(card)
    # Sort the list of digits in descending order
    digits.sort(reverse=True)
    # Initialize a variable to store the largest multiple of 90
    largest_multiple_of_90 = 0
    # Iterate through the digits and check if they form a multiple of 90
    for i in range(len(digits)):
        current_digit = digits[i]
        # If the current digit is 0, break the loop
        if current_digit == 0:
            break
        # If the current digit is 5 and the next digit is 0, add 50 to the largest multiple of 90
        if current_digit == 5 and i + 1 < len(digits) and digits[i + 1] == 0:
            largest_multiple_of_90 += 50
            # If the current digit is 5 and the next digit is not 0, add 5 to the largest multiple of 90
        elif current_digit == 5:
            largest_multiple_of_90 += 5
    # Return the largest multiple of 90
    return largest_multiple_of_90

def main():
    # Read the number of cards and the cards from stdin
    n = int(input())
    cards = list(map(int, input().split()))
    # Call the get_largest_multiple_of_90 function and print the result
    print(get_largest_multiple_of_90(cards))

if __name__ == '__main__':
    main()

