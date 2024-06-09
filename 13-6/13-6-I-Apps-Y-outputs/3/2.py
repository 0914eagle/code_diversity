
def get_move_count(n, a):
    # Initialize variables
    alice_moves = 0
    bob_moves = 0
    alice_total = 0
    bob_total = 0
    
    # Loop through each candy
    for i in range(n):
        # Alice's turn
        if i % 2 == 0:
            alice_total += a[i]
            alice_moves += 1
        
        # Bob's turn
        else:
            bob_total += a[i]
            bob_moves += 1
        
        # Check if the game has ended
        if alice_total > bob_total:
            break
        elif bob_total > alice_total:
            break
    
    # Return the number of moves
    return alice_moves, bob_moves

def get_total_sweets(n, a):
    # Initialize variables
    alice_total = 0
    bob_total = 0
    
    # Loop through each candy
    for i in range(n):
        # Alice's turn
        if i % 2 == 0:
            alice_total += a[i]
        
        # Bob's turn
        else:
            bob_total += a[i]
    
    # Return the total sweets eaten
    return alice_total, bob_total

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        moves = get_move_count(n, a)
        alice_total, bob_total = get_total_sweets(n, a)
        print(moves[0], alice_total, bob_total)

