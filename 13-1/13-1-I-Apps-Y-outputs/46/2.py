
def get_move_count(n, a):
    # Initialize variables to track the number of moves and the total size of candies eaten by Alice and Bob
    move_count = 0
    alice_total = 0
    bob_total = 0
    
    # Loop through the candies from left to right
    for i in range(n):
        # Check if it's Alice's turn
        if move_count % 2 == 0:
            # Alice eats one candy and adds its size to her total
            alice_total += a[i]
        else:
            # Bob eats one candy and adds its size to his total
            bob_total += a[n-i-1]
        
        # Increment the move count
        move_count += 1
        
        # Check if the total size of candies eaten by either player is greater than the other player's total
        if alice_total > bob_total:
            # If so, break out of the loop
            break
    
    # Return the move count and the total sizes of candies eaten by Alice and Bob
    return move_count, alice_total, bob_total

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        move_count, alice_total, bob_total = get_move_count(n, a)
        print(move_count, alice_total, bob_total)

