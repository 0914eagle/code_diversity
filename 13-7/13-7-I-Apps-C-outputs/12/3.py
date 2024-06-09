
def solve(n, m):
    # Initialize the playing schedule
    schedule = []

    # Iterate over each round
    for round in range(1, m * n + 1):
        # Initialize the games for this round
        games = []

        # Iterate over each player
        for player in range(1, n + 1):
            # Find the opponent for this player
            opponent = (player % m) + 1

            # Add the game to the schedule
            games.append("A" + str(player) + "-B" + str(opponent))

        # Add the games for this round to the schedule
        schedule.append(" ".join(games))

    # Return the playing schedule
    return schedule

