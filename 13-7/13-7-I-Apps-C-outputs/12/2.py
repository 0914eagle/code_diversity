
def schedule_tournament(n, m):
    # Initialize an empty playing schedule
    schedule = []

    # Iterate over each round
    for round in range(1, (m-1)*n+2):
        # Initialize an empty list of games for this round
        games = []

        # Iterate over each team
        for team in range(m):
            # Iterate over each player in the team
            for player in range(n):
                # If this is not the home team, add a game to the schedule
                if team != 0:
                    games.append("A" + str(player+1) + "-B" + str(player+1))

        # Add the list of games for this round to the schedule
        schedule.append(games)

    # Return the playing schedule
    return schedule

