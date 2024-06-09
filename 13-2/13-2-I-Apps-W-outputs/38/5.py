
def f1(n, k, a):
    # Initialize variables
    line = a
    winner = 0
    games_won = 0
    
    # Play games until someone wins k games in a row
    while games_won < k:
        # Play game between first two players
        if line[0] > line[1]:
            # First player wins
            line = line[1:] + [line[0]]
            games_won += 1
        else:
            # Second player wins
            line = line[2:] + [line[0], line[1]]
            games_won = 0
        
        # Update winner
        if games_won == k:
            winner = line[0]
    
    # Return power of winner
    return winner

def f2(...):
    ...

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    a = list(map(int, input().split()))
    print(f1(n, k, a))

