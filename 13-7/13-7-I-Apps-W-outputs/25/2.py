
def get_number_of_switches(n, teams):
    # Initialize a dictionary to keep track of the teams and their corresponding seats
    team_seats = {}
    for i, team in enumerate(teams):
        if team not in team_seats:
            team_seats[team] = [i]
        else:
            team_seats[team].append(i)

    # Initialize a variable to keep track of the number of switches
    switches = 0

    # Iterate through the teams and their corresponding seats
    for team, seats in team_seats.items():
        # Sort the seats in ascending order
        sorted_seats = sorted(seats)

        # Iterate through the sorted seats and check if they are in the correct order
        for i in range(len(sorted_seats) - 1):
            if sorted_seats[i + 1] - sorted_seats[i] != 1:
                # If the seats are not in the correct order, increment the number of switches
                switches += 1

    return switches

def main():
    n = int(input())
    teams = input()
    print(get_number_of_switches(n, teams))

if __name__ == '__main__':
    main()

