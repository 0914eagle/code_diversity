
import sys

def get_max_sum(cards, operations):
    # Initialize the maximum sum to 0
    max_sum = 0
    
    # Loop through each operation
    for operation in operations:
        # Get the number of cards to choose and the value to replace them with
        num_cards, value = operation
        
        # Loop through the cards and replace the values as specified by the operation
        for i in range(num_cards):
            cards[i] = value
    
    # Calculate the sum of the cards
    max_sum = sum(cards)
    
    # Return the maximum sum
    return max_sum

if __name__ == "__main__":
    # Read the input from stdin
    input_list = sys.stdin.read().split()
    n = int(input_list[0])
    m = int(input_list[1])
    cards = list(map(int, input_list[2:n+2]))
    operations = [list(map(int, input_list[i*2+2:i*2+4])) for i in range(m)]
    
    # Get the maximum sum
    max_sum = get_max_sum(cards, operations)
    
    # Print the maximum sum
    print(max_sum)

