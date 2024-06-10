
def is_possible(N, S):
    # Initialize a set to store the healths of the slimes
    healths = set()
    
    # Add the first slime's health to the set
    healths.add(S[0])
    
    # Loop through the remaining slimes and their healths
    for i in range(1, N):
        # Check if the current health is in the set
        if S[i] in healths:
            # If it is, return False
            return False
        # Add the current health to the set
        healths.add(S[i])
    
    # If all healths are unique, return True
    return True

def main():
    # Read the number of slimes and the healths of the slimes from stdin
    N = int(input())
    S = list(map(int, input().split()))
    
    # Check if the healths of the slimes can be set to make the multiset equal to S
    if is_possible(N, S):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

