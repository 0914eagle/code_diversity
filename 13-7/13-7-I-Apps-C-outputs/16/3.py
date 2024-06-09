
def solve(x, y):
    # Initialize the number of oranges and apples
    oranges = x
    apples = y
    
    # Initialize the sequence of cards
    sequence = []
    
    # While there are still oranges and apples in the bag
    while oranges > 0 and apples > 0:
        # Add a card with letter 'A' to the sequence
        sequence.append('A')
        
        # Give all oranges to Bob
        oranges = 0
        
        # Give all apples to Alice
        apples = 0
        
        # Remove the last card from the sequence
        sequence.pop()
        
        # Add a card with letter 'B' to the sequence
        sequence.append('B')
        
        # Give all oranges to Alice
        oranges = 0
        
        # Give all apples to Bob
        apples = 0
        
        # Remove the last card from the sequence
        sequence.pop()
    
    # If there are still oranges and apples in the bag, return Impossible
    if oranges > 0 or apples > 0:
        return 'Impossible'
    
    # Return the sequence of cards
    return ''.join(sequence)

