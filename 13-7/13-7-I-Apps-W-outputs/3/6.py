
def get_healths(N, S):
    # Initialize a list to store the healths of the slimes
    healths = [0]
    
    # Loop through each second, starting from the second slime
    for i in range(1, N):
        # Loop through each health in the multiset S
        for j in range(len(S)):
            # If the current health is not already in the list of healths, add it
            if S[j] not in healths:
                healths.append(S[j])
        # Sort the list of healths in ascending order
        healths.sort()
    
    # Return the list of healths
    return healths

def main():
    # Read the input from stdin
    N = int(input())
    S = list(map(int, input().split()))
    
    # Call the get_healths function and print the result
    print("Yes" if get_healths(N, S) == S else "No")

if __name__ == '__main__':
    main()

