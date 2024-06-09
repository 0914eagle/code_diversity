
def solve(x, y):
    # Check if x and y are positive
    if x <= 0 or y <= 0:
        return "Impossible"
    
    # Initialize the number of oranges and apples Alice and Bob have
    alice_oranges = x
    alice_apples = 0
    bob_oranges = 0
    bob_apples = y
    
    # Initialize the number of cards left to play
    cards_left = x + y - 1
    
    # Initialize the sequence of cards
    sequence = []
    
    # While there are still cards left to play
    while cards_left > 0:
        # Check if Alice has more oranges than apples
        if alice_oranges > alice_apples:
            # Add a card with letter 'A' to the sequence
            sequence.append("A")
            # Give all the oranges to Bob
            bob_oranges += alice_oranges
            # Set Alice's oranges to 0
            alice_oranges = 0
        # Check if Alice has more apples than oranges
        elif alice_apples > alice_oranges:
            # Add a card with letter 'B' to the sequence
            sequence.append("B")
            # Give all the apples to Alice
            alice_apples += bob_apples
            # Set Bob's apples to 0
            bob_apples = 0
        # Check if Alice and Bob have the same number of oranges and apples
        else:
            # Add a card with letter 'A' to the sequence
            sequence.append("A")
            # Give all the oranges to Bob
            bob_oranges += alice_oranges
            # Set Alice's oranges to 0
            alice_oranges = 0
            # Give all the apples to Alice
            alice_apples += bob_apples
            # Set Bob's apples to 0
            bob_apples = 0
        
        # Decrement the number of cards left to play
        cards_left -= 1
    
    # Check if the number of oranges and apples is the same for Alice and Bob
    if alice_oranges == bob_oranges and alice_apples == bob_apples:
        # Return the sequence of cards
        return "".join(sequence)
    else:
        # Return "Impossible" if the sequence of cards does not exist
        return "Impossible"

