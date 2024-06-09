
def get_move_count(n, a):
    # Initialize variables
    alice_move_count = 0
    bob_move_count = 0
    alice_candies_eaten = 0
    bob_candies_eaten = 0
    
    # Loop through each candy
    for i in range(n):
        # Alice's turn
        if i % 2 == 0:
            # Check if Alice can eat at least one candy
            if alice_candies_eaten < bob_candies_eaten:
                # Alice eats one candy
                alice_candies_eaten += a[i]
                alice_move_count += 1
            else:
                # Alice cannot eat any more candies
                break
        # Bob's turn
        else:
            # Check if Bob can eat at least one candy
            if bob_candies_eaten < alice_candies_eaten:
                # Bob eats one candy
                bob_candies_eaten += a[i]
                bob_move_count += 1
            else:
                # Bob cannot eat any more candies
                break
    
    # Return the number of moves
    return alice_move_count + bob_move_count

def get_candies_eaten(n, a, player):
    # Initialize variables
    candies_eaten = 0
    move_count = 0
    
    # Loop through each candy
    for i in range(n):
        # Check if it's the player's turn
        if i % 2 == player:
            # Check if the player can eat at least one candy
            if candies_eaten < move_count:
                # Player eats one candy
                candies_eaten += a[i]
                move_count += 1
            else:
                # Player cannot eat any more candies
                break
    
    # Return the number of candies eaten
    return candies_eaten

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        move_count = get_move_count(n, a)
        alice_candies_eaten = get_candies_eaten(n, a, 0)
        bob_candies_eaten = get_candies_eaten(n, a, 1)
        print(move_count, alice_candies_eaten, bob_candies_eaten)

