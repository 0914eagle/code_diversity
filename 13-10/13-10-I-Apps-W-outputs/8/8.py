
def get_largest_multiple_of_90(cards):
    # Initialize a list to store the possible numbers
    numbers = []
    
    # Iterate over the cards and create all possible numbers
    for i in range(len(cards)):
        for j in range(i+1, len(cards)):
            number = int("".join(map(str, cards[i:j])))
            numbers.append(number)
    
    # Filter out numbers that are not multiples of 90
    numbers = list(filter(lambda x: x % 90 == 0, numbers))
    
    # Return the largest number or -1 if no multiple of 90 exists
    return max(numbers) if numbers else -1

def main():
    # Read the number of cards and the cards from stdin
    n = int(input())
    cards = list(map(int, input().split()))
    
    # Call the function to get the largest multiple of 90
    result = get_largest_multiple_of_90(cards)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

