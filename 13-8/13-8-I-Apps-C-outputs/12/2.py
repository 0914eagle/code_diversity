
def get_suspects(n, p):
    # Initialize a set to store the suspects
    suspects = set()
    
    # Iterate over the input list
    for i in range(n):
        # Add the two suspects named by the current coder to the set
        suspects.add(i + 1)
        suspects.add(i + 2)
    
    # Return the number of possible two-suspect sets
    return len(suspects)

def main():
    # Read the input
    n, p = map(int, input().split())
    input_list = [tuple(map(int, input().split())) for _ in range(n)]
    
    # Call the get_suspects function
    result = get_suspects(n, p)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

