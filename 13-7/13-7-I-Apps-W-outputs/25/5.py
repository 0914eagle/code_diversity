
def get_min_switches(n, teams):
    # Initialize variables
    team_counts = {"A": 0, "B": 0, "C": 0}
    switches = 0

    # Count the number of people on each team
    for team in teams:
        team_counts[team] += 1

    # Loop through the teams and count the number of switches needed for each team
    for team in teams:
        if team_counts[team] == 0:
            continue
        team_size = team_counts[team]
        switches += team_size - 1

    return switches

def main():
    n = int(input())
    teams = input()
    print(get_min_switches(n, teams))

if __name__ == '__main__':
    main()

