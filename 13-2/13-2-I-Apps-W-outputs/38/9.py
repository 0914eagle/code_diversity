
def f1(n, k, a):
    # Initialize variables
    line = a
    winner = 0
    games_won = 0
    
    # Loop through the line of players
    while len(line) > 1:
        # Play a game between the first two players
        if line[0] > line[1]:
            # Player 1 wins
            games_won += 1
        else:
            # Player 2 wins
            games_won = 0
        # Send the loser to the end of the line
        line.append(line.pop(0))
        # Check if the winner has won k games in a row
        if games_won == k:
            # The winner is the first player in the line
            winner = line[0]
            break
    
    return winner

def f2(...):
    ...

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    a = list(map(int, input().split()))
    print(f1(n, k, a))

