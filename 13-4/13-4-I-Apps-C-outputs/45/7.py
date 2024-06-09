
def f1(n, k, a):
    # Calculate the sum of the cows in each pile
    sum_of_cows = sum(a)
    
    # Calculate the maximum number of cows that can be removed in a single move
    max_cows = k * (n // 2)
    
    # If the sum of the cows is odd, then Kevin wins
    if sum_of_cows % 2 == 1:
        return "Kevin"
    
    # If the sum of the cows is even and the maximum number of cows that can be removed in a single move is greater than or equal to the sum of the cows, then Nicky wins
    if sum_of_cows % 2 == 0 and max_cows >= sum_of_cows:
        return "Nicky"
    
    # Otherwise, Kevin wins
    return "Kevin"

def f2(n, k, a):
    # Initialize the game state
    game_state = a
    
    # Initialize the current player
    current_player = "Kevin"
    
    # Loop until a player wins
    while True:
        # If the current player is Kevin, they move first
        if current_player == "Kevin":
            # Remove a single cow from a chosen non-empty pile
            game_state = f1(n, k, game_state)
        
        # If the current player is Nicky, they move second
        else:
            # Choose a pile of cows with even size 2·x (x > 0), and replace it with k piles of x cows each
            game_state = f2(n, k, game_state)
        
        # Check if the game is over
        if len(game_state) == 0:
            # If the game is over and the current player is Kevin, then Nicky wins
            if current_player == "Kevin":
                return "Nicky"
            # If the game is over and the current player is Nicky, then Kevin wins
            else:
                return "Kevin"
        
        # Switch the current player
        if current_player == "Kevin":
            current_player = "Nicky"
        else:
            current_player = "Kevin"

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(f2(n, k, a))

