
def get_move_count(n, a):
    # Initialize variables to keep track of the move count and the total size of candies eaten by Alice and Bob
    move_count = 1
    alice_total = a[0]
    bob_total = 0
    
    # Loop through the remaining candies
    for i in range(1, n):
        # Check if Alice or Bob has eaten all the remaining candies
        if alice_total >= bob_total + a[i]:
            # Alice has eaten all the remaining candies, so the game ends
            break
        elif bob_total >= alice_total + a[i]:
            # Bob has eaten all the remaining candies, so the game ends
            break
        else:
            # Neither Alice nor Bob has eaten all the remaining candies, so the game continues
            move_count += 1
            alice_total += a[i]
            bob_total += a[n-i]
    
    # Return the move count and the total size of candies eaten by Alice and Bob
    return move_count, alice_total, bob_total

def get_output(n, a):
    move_count, alice_total, bob_total = get_move_count(n, a)
    return str(move_count) + " " + str(alice_total) + " " + str(bob_total)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(get_output(n, a))

