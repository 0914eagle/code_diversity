
def solve(n, m):
    # Initialize the playing schedule as an empty list
    playing_schedule = []

    # Loop through each round
    for round in range(1, m * n + 1):
        # Initialize the games list for this round
        games = []

        # Loop through each team
        for team in range(1, m + 1):
            # Loop through each player in the team
            for player in range(1, n + 1):
                # Check if the player is not in the same team as the current player
                if team != round:
                    # Add the game to the games list
                    games.append("A" + str(player) + "-B" + str(team))

        # Add the games list to the playing schedule
        playing_schedule.append(" ".join(games))

    # Return the playing schedule
    return playing_schedule

