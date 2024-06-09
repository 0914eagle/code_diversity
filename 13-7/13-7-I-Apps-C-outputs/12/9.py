
def solve(n, m):
    # Initialize the playing schedule as an empty list
    schedule = []

    # Iterate over each round
    for round in range(1, (m-1)*n+2):
        # Initialize the games list for this round
        games = []

        # Iterate over each player in each team
        for i in range(1, m+1):
            for j in range(1, n+1):
                # If this is not the current player, add them to the games list
                if i != j:
                    games.append(f"A{i}{j}")

        # Add the games list for this round to the playing schedule
        schedule.append(" ".join(games))

    # Return the playing schedule
    return schedule

