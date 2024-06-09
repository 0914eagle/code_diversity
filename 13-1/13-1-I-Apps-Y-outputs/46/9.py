
def get_move_count(n, a):
    # Initialize variables to track the number of moves and the total size of candies eaten by Alice and Bob
    move_count = 0
    alice_total = 0
    bob_total = 0
    
    # Loop through the candies from left to right
    for i in range(n):
        # Check if Alice or Bob should make the next move
        if move_count % 2 == 0:
            # Alice makes the move
            alice_total += a[i]
        else:
            # Bob makes the move
            bob_total += a[n-i-1]
        
        # Increment the move count
        move_count += 1
    
    # Return the number of moves and the total size of candies eaten by Alice and Bob
    return move_count, alice_total, bob_total

