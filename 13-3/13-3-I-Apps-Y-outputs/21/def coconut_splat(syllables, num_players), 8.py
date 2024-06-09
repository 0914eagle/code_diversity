
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
            current_player = (current_player + 1) % num_players
            # If the touched player has their hands folded, split them into two fists
            if touched_player in players:
                players.remove(touched_player)
                players.append(touched_player)
                players.append(touched_player)
        # If the touched player has their hands turned palm down, remove them from the game
        if touched_player in players:
            players.remove(touched_player)
        # Update the number of players left in the game
        num_players_left = len(players)
    # Return the number of the player who is left
    return players[0]

