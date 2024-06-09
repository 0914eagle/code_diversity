
def get_move_count(n, a):
    # Initialize variables to track the number of moves and the total size of candies eaten by Alice and Bob
    move_count = 0
    alice_size = 0
    bob_size = 0
    
    # Loop through the candies from left to right
    for i in range(n):
        # Alice eats the current candy
        alice_size += a[i]
        move_count += 1
        
        # Bob eats the current candy if the total size of candies eaten by Alice is greater than the total size of candies eaten by Bob
        if alice_size > bob_size:
            bob_size += a[n-i-1]
            move_count += 1
        
    # Return the number of moves and the total size of candies eaten by Alice and Bob
    return move_count, alice_size, bob_size

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        move_count, alice_size, bob_size = get_move_count(n, a)
        print(move_count, alice_size, bob_size)

if __name__ == '__main__':
    main()

