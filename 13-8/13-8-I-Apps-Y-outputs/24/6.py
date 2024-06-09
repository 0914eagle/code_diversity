
def solve(s_a, s_b, s_c):
    # Initialize the decks of the players
    alice = deque(s_a)
    bob = deque(s_b)
    charlie = deque(s_c)
    
    # Game ends when a player's deck is empty
    while alice and bob and charlie:
        # Alice takes the first turn
        if alice:
            alice.popleft()
        # Bob takes the turn if the top card of Alice's deck is 'a'
        elif bob and alice and alice[0] == 'a':
            bob.popleft()
        # Charlie takes the turn if the top card of Alice's deck is 'c'
        elif charlie and alice and alice[0] == 'c':
            charlie.popleft()
    
    # Return the winner
    if alice:
        return 'A'
    elif bob:
        return 'B'
    else:
        return 'C'

