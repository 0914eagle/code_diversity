
def input_slime_healths(n):
    
    healths = [int(input()) for _ in range(n)]
    return healths

def set_slime_healths(n, healths):
    
    # Initialize the health of the first slime
    health = healths[0]
    # Initialize the number of slimes that have been spawned
    num_slimes = 1
    # Loop through the remaining healths in the list
    for i in range(1, n):
        # Spawn a new slime with a health that is one less than the current slime
        healths.append(health - 1)
        # Increment the number of slimes that have been spawned
        num_slimes += 1
        # Update the health of the current slime
        health = healths[i]
    # Check if the number of slimes that have been spawned is equal to 2^N
    if num_slimes == 2**n:
        return True
    else:
        return False

def main():
    
    # Input the number of slimes from standard input
    n = int(input())
    # Input the healths of the slimes from standard input
    healths = input_slime_healths(n)
    # Set the healths of the slimes so that the multiset of the healths of the 2^N slimes that will exist in N seconds equals the given multiset S
    result = set_slime_healths(n, healths)
    # Print the result
    if result:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

