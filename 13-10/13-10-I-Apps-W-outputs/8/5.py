
def largest_multiple_of_90(cards):
    # Initialize a list to store the numbers
    numbers = []
    # Iterate through the cards
    for card in cards:
        # If the card is 5, append 5 to the list
        if card == 5:
            numbers.append(5)
        # If the card is 0, append 0 to the list
        elif card == 0:
            numbers.append(0)
    # If the list is empty, return -1
    if not numbers:
        return -1
    # Initialize a variable to store the maximum number
    max_num = 0
    # Iterate through the numbers
    for num in numbers:
        # If the number is 5, multiply it by 10 and add it to the maximum number
        if num == 5:
            max_num = (max_num * 10) + num
        # If the number is 0, multiply it by 10 and add it to the maximum number
        elif num == 0:
            max_num = (max_num * 10) + num
    # Return the maximum number
    return max_num

def main():
    # Input the number of cards
    n = int(input())
    # Input the cards
    cards = [int(x) for x in input().split()]
    # Call the largest_multiple_of_90 function
    result = largest_multiple_of_90(cards)
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

