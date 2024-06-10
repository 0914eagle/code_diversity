
def is_possible(N, S):
    # Initialize a list to store the healths of the slimes
    healths = [0]
    
    # Loop through each second
    for i in range(N):
        # Loop through each slime in the previous second
        for j in range(len(healths)):
            # Spawn a new slime with a health that is one less than the current slime
            healths.append(healths[j] - 1)
    
    # Check if the multiset of the healths is equal to S
    return sorted(healths) == sorted(S)

def main():
    # Read the input from stdin
    N = int(input())
    S = list(map(int, input().split()))
    
    # Check if it is possible to make the multiset of the healths equal to S
    if is_possible(N, S):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

