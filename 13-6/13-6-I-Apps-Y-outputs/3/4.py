
def get_move_count(n, a):
    # Initialize variables
    alice_moves = 0
    bob_moves = 0
    alice_total = 0
    bob_total = 0

    # Loop through the candies
    for i in range(n):
        # Alice's turn
        if i % 2 == 0:
            alice_total += a[i]
            alice_moves += 1

        # Bob's turn
        else:
            bob_total += a[i]
            bob_moves += 1

            # Check if Bob's move is greater than Alice's previous move
            if bob_total > alice_total:
                break

    # Return the number of moves
    return alice_moves, bob_moves

def get_total_sweets(n, a):
    # Initialize variables
    alice_total = 0
    bob_total = 0

    # Loop through the candies
    for i in range(n):
        # Alice's turn
        if i % 2 == 0:
            alice_total += a[i]

        # Bob's turn
        else:
            bob_total += a[i]

    # Return the total number of sweets eaten
    return alice_total, bob_total

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        alice_moves, bob_moves = get_move_count(n, a)
        alice_total, bob_total = get_total_sweets(n, a)
        print(alice_moves, bob_total, bob_total)

