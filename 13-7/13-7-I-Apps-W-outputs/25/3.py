
def get_number_of_switches(n, team_arrangement):
    # Initialize variables
    team_A = []
    team_B = []
    team_C = []
    switches = 0

    # Separate the teams
    for i in range(n):
        if team_arrangement[i] == "A":
            team_A.append(i)
        elif team_arrangement[i] == "B":
            team_B.append(i)
        else:
            team_C.append(i)

    # Check if teams are already lined up correctly
    if team_A == list(range(n)) or team_B == list(range(n)) or team_C == list(range(n)):
        return 0

    # Find the minimum number of switches required to line up the teams
    for i in range(n):
        if team_A[i] != i:
            switches += 1
        if team_B[i] != i + 1:
            switches += 1
        if team_C[i] != i + 2:
            switches += 1

    return switches

def main():
    n = int(input())
    team_arrangement = input()
    print(get_number_of_switches(n, team_arrangement))

if __name__ == '__main__':
    main()

