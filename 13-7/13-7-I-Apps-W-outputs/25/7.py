
def get_min_switches(seating_arrangement):
    # Initialize variables
    team_a = []
    team_b = []
    team_c = []
    switches = 0

    # Separate the seating arrangement into teams
    for i in range(len(seating_arrangement)):
        if seating_arrangement[i] == "A":
            team_a.append(i)
        elif seating_arrangement[i] == "B":
            team_b.append(i)
        else:
            team_c.append(i)

    # Check if teams are already lined up correctly
    if team_a == list(range(len(team_a))) and team_b == list(range(len(team_b))) and team_c == list(range(len(team_c))):
        return switches

    # Find the minimum number of switches required to line up the teams correctly
    for i in range(len(seating_arrangement)):
        if seating_arrangement[i] != "A" and team_a[0] != i:
            switches += 1
        if seating_arrangement[i] != "B" and team_b[0] != i:
            switches += 1
        if seating_arrangement[i] != "C" and team_c[0] != i:
            switches += 1

    return switches

def main():
    seating_arrangement = input()
    print(get_min_switches(seating_arrangement))

if __name__ == '__main__':
    main()

