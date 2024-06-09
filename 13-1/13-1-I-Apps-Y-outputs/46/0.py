
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
    
    # Return the move counts
    return alice_move_count, bob_move_count

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
            bob_total += a[n-i-1]
    
    # Return the total sweets
    return alice_total, bob_total

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        move_count = get_move_count(n, a)
        total_sweets = get_total_sweets(n, a)
        print(move_count[0], move_count[1], total_sweets[0], total_sweets[1])

