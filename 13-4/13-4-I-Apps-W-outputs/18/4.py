
def assign_players(n, m):
    # Initialize a list to store the players and their integers
    players = [(i, i) for i in range(1, n + 1)]
    # Initialize a list to store the assignments
    assignments = []
    # Loop through each round
    for i in range(n):
        # Find the two players with the smallest integers
        a, b = sorted(players)[0], sorted(players)[1]
        # Assign them to the same playing field
        assignments.append((a[0], b[0]))
        # Increment the integers of the players
        players[a[1] - 1] = (a[0], a[1] + 1)
        players[b[1] - 1] = (b[0], b[1] + 1)
        # Wrap around the integers if necessary
        players[a[1] - 1] = (a[0], 1 if a[1] > n else a[1])
        players[b[1] - 1] = (b[0], 1 if b[1] > n else b[1])
    # Return the assignments
    return assignments

def main():
    n, m = map(int, input().split())
    assignments = assign_players(n, m)
    for assignment in assignments:
        print(*assignment)

if __name__ == '__main__':
    main()

