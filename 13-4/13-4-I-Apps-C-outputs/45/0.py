
def f1(n, k, a):
    # Calculate the sum of the cows in each pile
    sum_of_cows = sum(a)
    
    # Calculate the number of cows that Kevin can remove
    kevin_cows = sum_of_cows // 2
    
    # Calculate the number of cows that Nicky can remove
    nicky_cows = sum_of_cows - kevin_cows
    
    # Check if Kevin has more cows than Nicky
    if kevin_cows > nicky_cows:
        return "Kevin"
    elif kevin_cows < nicky_cows:
        return "Nicky"
    else:
        return "Tie"

def f2(n, k, a):
    # Initialize the game state
    game_state = a
    
    # Initialize the number of cows removed by each player
    kevin_cows = 0
    nicky_cows = 0
    
    # Loop until a player has removed all the cows
    while sum(game_state) > 0:
        # Check if it is Kevin's turn
        if kevin_cows % 2 == 0:
            # Kevin removes a cow from a pile
            game_state = f1(n, k, game_state)
            kevin_cows += 1
        else:
            # Nicky removes a cow from a pile
            game_state = f2(n, k, game_state)
            nicky_cows += 1
    
    # Check if Kevin has more cows than Nicky
    if kevin_cows > nicky_cows:
        return "Kevin"
    elif kevin_cows < nicky_cows:
        return "Nicky"
    else:
        return "Tie"

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(f2(n, k, a))

