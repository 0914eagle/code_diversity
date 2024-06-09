
import sys

def get_max_sum(cards, operations):
    # Initialize the maximum sum to 0
    max_sum = 0
    # Loop through the operations
    for operation in operations:
        # Get the number of cards to choose and the value to replace them with
        num_cards, value = operation
        # Get the indices of the cards to choose
        indices = list(range(num_cards))
        # Replace the values on the chosen cards with the given value
        for index in indices:
            cards[index] = value
        # Calculate the sum of the cards after the operation
        sum_after_operation = sum(cards)
        # Update the maximum sum if necessary
        if sum_after_operation > max_sum:
            max_sum = sum_after_operation
    # Return the maximum sum
    return max_sum

if __name__ == '__main__':
    # Get the number of cards and operations from stdin
    num_cards, num_operations = map(int, input().split())
    # Get the values on the cards from stdin
    cards = list(map(int, input().split()))
    # Get the operations from stdin
    operations = []
    for _ in range(num_operations):
        operations.append(list(map(int, input().split())))
    # Get the maximum sum
    max_sum = get_max_sum(cards, operations)
    # Print the maximum sum
    print(max_sum)

