
def get_move_count(n, a):
    # Initialize variables
    alice_move_count = 0
    bob_move_count = 0
    alice_total = 0
    bob_total = 0
    
    # Loop through each candy
    for i in range(n):
        # Alice's turn
        if i % 2 == 0:
            alice_total += a[i]
            alice_move_count += 1
        
        # Bob's turn
        else:
            bob_total += a[i]
            bob_move_count += 1
        
        # Check if either player has won
        if alice_total > bob_total:
            break
        elif bob_total > alice_total:
            break
    
    # Return the move count and total sizes
    return alice_move_count, bob_move_count, alice_total, bob_total

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        move_count, alice_move_count, bob_move_count, alice_total, bob_total = get_move_count(n, a)
        print(move_count, alice_move_count, bob_move_count)

if __name__ == '__main__':
    main()

