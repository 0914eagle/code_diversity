
def get_moves(n, a):
    # Initialize variables
    alice_moves = 0
    bob_moves = 0
    alice_sum = 0
    bob_sum = 0
    
    # Loop through each candy
    for i in range(n):
        # Alice's turn
        if i % 2 == 0:
            alice_sum += a[i]
            alice_moves += 1
        # Bob's turn
        else:
            bob_sum += a[i]
            bob_moves += 1
        
        # Check if either player can make a move
        if alice_sum > bob_sum:
            bob_moves += 1
            alice_sum = 0
        elif bob_sum > alice_sum:
            alice_moves += 1
            bob_sum = 0
    
    # Return the number of moves
    return alice_moves, bob_moves

def get_sizes(n, a):
    # Initialize variables
    alice_sum = 0
    bob_sum = 0
    
    # Loop through each candy
    for i in range(n):
        # Alice's turn
        if i % 2 == 0:
            alice_sum += a[i]
        # Bob's turn
        else:
            bob_sum += a[i]
    
    # Return the total sizes
    return alice_sum, bob_sum

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        moves = get_moves(n, a)
        sizes = get_sizes(n, a)
        print(moves[0], sizes[0], sizes[1])

