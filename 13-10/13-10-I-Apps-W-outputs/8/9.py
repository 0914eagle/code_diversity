
def get_largest_divisible_by_90(cards):
    # Initialize a list to store the numbers
    numbers = []
    
    # Iterate over the cards
    for card in cards:
        # If the card is 0, append 0 to the list
        if card == 0:
            numbers.append(0)
        # If the card is 5, append 5 to the list
        elif card == 5:
            numbers.append(5)
    
    # Initialize a variable to store the largest number divisible by 90
    largest_divisible_by_90 = -1
    
    # Iterate over the numbers
    for i in range(len(numbers)):
        # If the number is 0, break the loop
        if numbers[i] == 0:
            break
        # If the number is 5, append 5 to the list
        elif numbers[i] == 5:
            numbers.append(5)
    
    # Iterate over the numbers
    for i in range(len(numbers)):
        # If the number is 0, break the loop
        if numbers[i] == 0:
            break
        # If the number is 5, append 5 to the list
        elif numbers[i] == 5:
            numbers.append(5)
    
    # Initialize a variable to store the sum of the numbers
    sum_of_numbers = 0
    
    # Iterate over the numbers
    for number in numbers:
        # Add the number to the sum
        sum_of_numbers += number
    
    # If the sum is divisible by 90, set the largest number divisible by 90 to the sum
    if sum_of_numbers % 90 == 0:
        largest_divisible_by_90 = sum_of_numbers
    
    # Return the largest number divisible by 90
    return largest_divisible_by_90

def main():
    # Input the number of cards
    n = int(input())
    
    # Input the cards
    cards = [int(input()) for _ in range(n)]
    
    # Call the get_largest_divisible_by_90 function
    largest_divisible_by_90 = get_largest_divisible_by_90(cards)
    
    # Print the largest number divisible by 90
    print(largest_divisible_by_90)

if __name__ == '__main__':
    main()

