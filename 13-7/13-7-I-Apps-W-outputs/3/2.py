
def get_healths(N, S):
    # Initialize a list to store the healths of the slimes
    healths = []
    
    # Set the health of the first slime
    healths.append(S[0])
    
    # Loop through the remaining elements of S
    for i in range(1, len(S)):
        # Get the next element of S
        next_health = S[i]
        
        # Loop through the previous elements of S
        for j in range(i):
            # Get the previous element of S
            prev_health = S[j]
            
            # If the previous element is less than the next element, break the loop
            if prev_health < next_health:
                break
        
        # If the loop completes, it means that the next element is the smallest element in S
        # that is greater than or equal to the previous elements
        # Therefore, set the health of the next slime to the next element
        healths.append(next_health)
    
    # Return the healths of the slimes
    return healths

def main():
    # Read the input from stdin
    N = int(input())
    S = list(map(int, input().split()))
    
    # Call the get_healths function and print the result
    print("Yes") if get_healths(N, S) == S else print("No")

if __name__ == '__main__':
    main()

