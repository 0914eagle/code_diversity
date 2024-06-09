
def solve_tournament(n, m):
    # Initialize the playing schedule as a list of lists
    schedule = [[[] for _ in range(n)] for _ in range(m)]

    # Iterate over each team
    for i in range(m):
        # Iterate over each player in the team
        for j in range(n):
            # Find the opponent team and player
            opponent_team = (i + 1) % m
            opponent_player = (j + 1) % n

            # Add the game to the schedule
            schedule[i][j].append("A{}".format(j + 1))
            schedule[i][j].append("B{}".format(opponent_player + 1))

    # Flatten the schedule list
    flattened_schedule = [game for team in schedule for game in team]

    # Return the flattened schedule
    return flattened_schedule

