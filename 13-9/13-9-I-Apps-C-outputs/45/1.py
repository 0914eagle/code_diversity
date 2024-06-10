
def get_suspects(n, p):
    # Initialize a set to store the suspects
    suspects = set()
    
    # Iterate over the input array
    for i in range(n):
        # Add the two named coders to the set of suspects
        suspects.add(i + 1)
        suspects.add(input()[1])
    
    # Return the number of ways to choose two suspects such that at least p coders agree with the choice
    return len(suspects)

def main():
    # Read the input n and p
    n, p = map(int, input().split())
    
    # Call the get_suspects function and print the result
    print(get_suspects(n, p))

if __name__ == '__main__':
    main()

