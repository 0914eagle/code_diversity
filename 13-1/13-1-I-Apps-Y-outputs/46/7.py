
def get_moves(n, a):
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
        
        # Check if either player has won
        if alice_total > bob_total:
            break
        elif bob_total > alice_total:
            break
    
    # Return the number of moves and the total sizes eaten by Alice and Bob
    return alice_moves, bob_total, alice_total

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        alice_moves, bob_total, alice_total = get_moves(n, a)
        print(alice_moves, bob_total, alice_total)

if __name__ == '__main__':
    main()

