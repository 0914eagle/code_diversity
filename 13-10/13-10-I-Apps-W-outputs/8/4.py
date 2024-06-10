
def get_largest_multiple_of_90(cards):
    # Initialize a list to store the digits
    digits = []
    # Iterate through the cards
    for card in cards:
        # If the card is 5, add it to the list of digits
        if card == 5:
            digits.append(card)
    # If there are no 5s, return -1
    if not digits:
        return -1
    # Initialize a variable to store the largest multiple of 90
    largest_multiple = 0
    # Iterate through the digits
    for i in range(len(digits)):
        # If the number of digits is divisible by 3, add it to the largest multiple of 90
        if len(digits) % 3 == 0:
            largest_multiple += int("".join(map(str, digits)))
        # Remove the first digit and add the last digit to the end of the list
        digits.pop(0)
        digits.append(digits.pop(0))
    # Return the largest multiple of 90
    return largest_multiple

def main():
    # Accept the number of cards as input
    n = int(input())
    # Accept the cards as input
    cards = [int(i) for i in input().split()]
    # Call the function to get the largest multiple of 90
    largest_multiple = get_largest_multiple_of_90(cards)
    # Print the result
    print(largest_multiple)

if __name__ == '__main__':
    main()

