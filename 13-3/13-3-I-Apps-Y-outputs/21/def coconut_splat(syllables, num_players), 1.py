
def coconut_splat(syllables, num_players):
    # Initialize the list of players
    players = list(range(1, num_players+1))
    # Initialize the current player
    current_player = 1
    # Initialize the number of players still in the game
    num_players_left = num_players
    # Loop until only one player is left
    while num_players_left > 1:
        # Determine the player who will be touched
        touched_player = current_player
        # Loop through each syllable in the rhyme
        for _ in range(syllables):
            # Touch the next player's hand
            touched_player = (touched_player + 1) % num_players
        # Check if the touched player has folded hands
        if touched_player in players:
            # Split the coconut in half
            players.insert(players.index(touched_player) + 1, touched_player)
            # Move to the next player
            current_player = (current_player + 1) % num_players
        else:
            # The touched player has already been split, so move to the next player
            current_player = (current_player + 1) % num_players
        # Remove the touched player from the list
        players.remove(touched_player)
        # Decrement the number of players left
        num_players_left -= 1
    # Return the winner
    return players[0]

