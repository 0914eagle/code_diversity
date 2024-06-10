
def get_slime_healths(N, S):
    # Initialize a list to store the healths of the slimes
    slime_healths = []
    
    # Set the health of the first slime to any integer value of your choice
    slime_healths.append(4)
    
    # Loop through the remaining slimes and set their healths
    for i in range(1, N):
        # Get the health of the previous slime
        prev_slime_health = slime_healths[i - 1]
        
        # Set the health of the current slime to be one less than the previous slime
        slime_healths.append(prev_slime_health - 1)
    
    # Return the list of slime healths
    return slime_healths

def main():
    # Read the input from stdin
    N = int(input())
    S = list(map(int, input().split()))
    
    # Get the list of slime healths
    slime_healths = get_slime_healths(N, S)
    
    # Check if the multiset of the healths of the slimes is equal to S
    if sorted(slime_healths) == sorted(S):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

