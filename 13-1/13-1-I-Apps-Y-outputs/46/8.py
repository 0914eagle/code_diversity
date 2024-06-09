
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
            alice_move_count += 1
            alice_total += a[i]
            
            # Check if Bob needs to eat more candies
            if bob_total < alice_total:
                bob_move_count += 1
                bob_total += a[n-i-1]
        
        # Bob's turn
        else:
            bob_move_count += 1
            bob_total += a[n-i-1]
            
            # Check if Alice needs to eat more candies
            if alice_total < bob_total:
                alice_move_count += 1
                alice_total += a[i]
    
    # Return the number of moves and the total sizes eaten by Alice and Bob
    return alice_move_count, alice_total, bob_move_count, bob_total

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        alice_move_count, alice_total, bob_move_count, bob_total = get_move_count(n, a)
        print(alice_move_count, alice_total, bob_move_count, bob_total)

