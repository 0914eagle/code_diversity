
import sys

def get_max_sum(cards, operations):
    # Initialize the maximum sum to 0
    max_sum = 0
    
    # Loop through each operation
    for operation in operations:
        # Get the number of cards to choose and the value to replace them with
        num_cards, value = operation
        
        # Find the indices of the cards to choose
        indices = sorted(random.sample(range(len(cards)), num_cards))
        
        # Replace the values of the chosen cards with the given value
        for index in indices:
            cards[index] = value
    
    # Calculate the sum of the cards
    max_sum = sum(cards)
    
    return max_sum

if __name__ == "__main__":
    # Read the input from stdin
    input_list = sys.stdin.read().split()
    n = int(input_list[0])
    m = int(input_list[1])
    cards = list(map(int, input_list[2:n+2]))
    operations = [list(map(int, input_list[i:i+2])) for i in range(n+2, n+2+2*m, 2)]
    
    # Get the maximum sum
    max_sum = get_max_sum(cards, operations)
    
    # Print the result
    print(max_sum)

