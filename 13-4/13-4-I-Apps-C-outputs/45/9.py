
def f1(n, k, a):
    # Calculate the sum of the cows in each pile
    sum_of_cows = sum(a)
    
    # Calculate the number of cows that Kevin can remove
    num_cows_kevin_can_remove = sum_of_cows // 2
    
    # Calculate the number of cows that Nicky can remove
    num_cows_nicky_can_remove = sum_of_cows - num_cows_kevin_can_remove
    
    # If Kevin removes all the cows, he wins
    if num_cows_kevin_can_remove == 0:
        return "Kevin"
    
    # If Nicky removes all the cows, he wins
    if num_cows_nicky_can_remove == 0:
        return "Nicky"
    
    # If neither player can remove all the cows, the game continues
    return "Game continues"

def f2(n, k, a):
    # Initialize the game state
    game_state = a
    
    # Initialize the number of cows removed by each player
    num_cows_kevin_removed = 0
    num_cows_nicky_removed = 0
    
    # Initialize the number of piles removed by each player
    num_piles_kevin_removed = 0
    num_piles_nicky_removed = 0
    
    # Initialize the winner
    winner = None
    
    # While the game is not over
    while winner is None:
        # If it is Kevin's turn
        if num_cows_kevin_removed < num_cows_nicky_removed:
            # Remove a cow from a pile
            game_state = f1(n, k, game_state)
            
            # Increment the number of cows removed by Kevin
            num_cows_kevin_removed += 1
            
            # If Kevin removes all the cows, he wins
            if num_cows_kevin_removed == num_cows_nicky_removed:
                winner = "Kevin"
        
        # If it is Nicky's turn
        else:
            # Remove a pile of cows
            game_state = f2(n, k, game_state)
            
            # Increment the number of piles removed by Nicky
            num_piles_nicky_removed += 1
            
            # If Nicky removes all the piles, he wins
            if num_piles_nicky_removed == num_piles_kevin_removed:
                winner = "Nicky"
    
    # Return the winner
    return winner

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(f2(n, k, a))

