
def get_move_count(n, a):
    # Initialize variables
    alice_move_count = 0
    bob_move_count = 0
    alice_candy_count = 0
    bob_candy_count = 0
    
    # Loop through each candy
    for i in range(n):
        # Alice's turn
        if i % 2 == 0:
            alice_candy_count += a[i]
            alice_move_count += 1
        
        # Bob's turn
        else:
            bob_candy_count += a[i]
            bob_move_count += 1
        
        # Check if either player has eaten all the candies
        if alice_candy_count > sum(a[i+1:]) or bob_candy_count > sum(a[:i]):
            break
    
    # Return the move count and candy count for both players
    return alice_move_count, bob_move_count, alice_candy_count, bob_candy_count

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        move_count, alice_move_count, bob_move_count, alice_candy_count, bob_candy_count = get_move_count(n, a)
        print(move_count, alice_move_count, bob_move_count)

if __name__ == '__main__':
    main()

