
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
        
        # Check if the game ends
        if alice_sum > bob_sum:
            break
        elif bob_sum > alice_sum:
            break
    
    # Return the number of moves and the total sum of candies eaten by Alice and Bob
    return alice_moves, bob_moves, alice_sum, bob_sum

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        alice_moves, bob_moves, alice_sum, bob_sum = get_moves(n, a)
        print(alice_moves, bob_moves, alice_sum, bob_sum)

if __name__ == '__main__':
    main()

