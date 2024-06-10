
def get_min_switches(n, teams):
    # Initialize variables
    team_a = 0
    team_b = 0
    team_c = 0
    switches = 0

    # Count the number of players on each team
    for i in range(n):
        if teams[i] == "A":
            team_a += 1
        elif teams[i] == "B":
            team_b += 1
        else:
            team_c += 1

    # Calculate the minimum number of switches required
    switches += abs(team_a - team_b)
    switches += abs(team_b - team_c)
    switches += abs(team_c - team_a)

    return switches

def main():
    n = int(input())
    teams = input()
    print(get_min_switches(n, teams))

if __name__ == '__main__':
    main()

