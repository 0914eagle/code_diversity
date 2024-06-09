
def get_move_count(n, a):
    # Initialize variables
    alice_move_count = 0
    bob_move_count = 0
    alice_total_size = 0
    bob_total_size = 0
    
    # Loop through each candy
    for i in range(n):
        # Alice's turn
        if i % 2 == 0:
            alice_move_count += 1
            alice_total_size += a[i]
            if alice_total_size > bob_total_size:
                break
        # Bob's turn
        else:
            bob_move_count += 1
            bob_total_size += a[i]
            if bob_total_size > alice_total_size:
                break
    
    # Return the move count and total sizes
    return alice_move_count, bob_move_count, alice_total_size, bob_total_size

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        alice_move_count, bob_move_count, alice_total_size, bob_total_size = get_move_count(n, a)
        print(alice_move_count, bob_move_count, alice_total_size, bob_total_size)

if __name__ == '__main__':
    main()

