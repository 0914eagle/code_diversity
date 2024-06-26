
def f1(n, k, a):
    # Initialize variables
    line = a
    winner = 0
    count = 0
    
    # Loop through the line of players
    while len(line) > 1:
        # Play a game between the first two players
        if line[0] > line[1]:
            # Player 1 wins
            winner = line[0]
            count += 1
        else:
            # Player 2 wins
            winner = line[1]
            count += 1
        
        # Remove the winner from the line
        line.remove(winner)
        
        # Add the winner to the end of the line
        line.append(winner)
        
        # Check if the winner has won k games in a row
        if count == k:
            break
    
    # Return the power of the winner
    return winner

def f2(n, k, a):
    # Initialize variables
    line = a
    winner = 0
    count = 0
    
    # Loop through the line of players
    while len(line) > 1:
        # Play a game between the first two players
        if line[0] > line[1]:
            # Player 1 wins
            winner = line[0]
            count += 1
        else:
            # Player 2 wins
            winner = line[1]
            count += 1
        
        # Remove the winner from the line
        line.remove(winner)
        
        # Add the winner to the end of the line
        line.append(winner)
        
        # Check if the winner has won k games in a row
        if count == k:
            break
    
    # Return the power of the winner
    return winner

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    a = list(map(int, input().split()))
    print(f1(n, k, a))
    print(f2(n, k, a))

