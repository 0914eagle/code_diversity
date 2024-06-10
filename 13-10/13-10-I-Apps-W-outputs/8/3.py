
def get_largest_divisible_number(cards):
    # Initialize a list to store the cards
    card_list = []
    
    # Iterate through the cards and append them to the list
    for card in cards:
        card_list.append(card)
    
    # Initialize a variable to store the largest divisible number
    largest_divisible_number = 0
    
    # Iterate through the cards and check if they are divisible by 90
    for i in range(len(card_list)):
        for j in range(i+1, len(card_list)):
            # Check if the sum of the cards is divisible by 90
            if (card_list[i] + card_list[j]) % 90 == 0:
                # Check if the sum is larger than the current largest divisible number
                if (card_list[i] + card_list[j]) > largest_divisible_number:
                    # Update the largest divisible number
                    largest_divisible_number = card_list[i] + card_list[j]
    
    # Return the largest divisible number
    return largest_divisible_number

def main():
    # Input the number of cards and the cards
    n = int(input())
    cards = list(map(int, input().split()))
    
    # Get the largest divisible number
    largest_divisible_number = get_largest_divisible_number(cards)
    
    # Print the result
    print(largest_divisible_number)

if __name__ == '__main__':
    main()

