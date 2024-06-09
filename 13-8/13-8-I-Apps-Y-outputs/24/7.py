
def solve(s_a, s_b, s_c):
    # Initialize the decks of the players
    alice = list(s_a)
    bob = list(s_b)
    charlie = list(s_c)
    
    # While all decks are not empty
    while alice and bob and charlie:
        # Alice takes the first turn
        current_player = "A"
        # If Alice's deck is not empty, discard the top card
        if alice:
            current_player = alice.pop(0)
        # If the current player's deck is empty, the game ends and the current player wins
        if not current_player:
            return "A"
        # If the current player is Bob, discard the top card in his deck
        if current_player == "B":
            bob.pop(0)
        # If the current player is Charlie, discard the top card in his deck
        if current_player == "C":
            charlie.pop(0)
    
    # If Alice's deck is empty, Bob wins
    if not alice:
        return "B"
    # If Bob's deck is empty, Charlie wins
    if not bob:
        return "C"
    # If Charlie's deck is empty, Alice wins
    if not charlie:
        return "A"

print(solve("aca", "accc", "ca"))

