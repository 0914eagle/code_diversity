
def get_min_switches(n, teams):
    # Initialize variables
    team_count = {"A": 0, "B": 0, "C": 0}
    switch_count = 0
    
    # Count the number of people on each team
    for team in teams:
        team_count[team] += 1
    
    # Loop through the teams and switch people if necessary
    for i in range(n):
        current_team = teams[i]
        next_team = teams[(i + 1) % n]
        if current_team != next_team:
            switch_count += 1
            teams[i] = next_team
    
    # Return the minimum number of switches needed
    return switch_count

def main():
    n = int(input())
    teams = input()
    print(get_min_switches(n, teams))

if __name__ == '__main__':
    main()

