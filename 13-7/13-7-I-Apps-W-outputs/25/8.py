
def get_min_switches(n, teams):
    # Initialize variables
    switches = 0
    team_a = []
    team_b = []
    team_c = []

    # Separate the teams
    for i in range(n):
        if teams[i] == "A":
            team_a.append(i)
        elif teams[i] == "B":
            team_b.append(i)
        else:
            team_c.append(i)

    # Check if teams are already lined up correctly
    if team_a == list(range(len(team_a))) and team_b == list(range(len(team_b))) and team_c == list(range(len(team_c))):
        return switches

    # Switch teams if necessary
    for i in range(n):
        if teams[i] != "A" and teams[i - 1] == "A":
            switches += 1
        elif teams[i] != "B" and teams[i - 1] == "B":
            switches += 1
        elif teams[i] != "C" and teams[i - 1] == "C":
            switches += 1

    return switches

def main():
    n = int(input())
    teams = input()
    print(get_min_switches(n, teams))

if __name__ == '__main__':
    main()

