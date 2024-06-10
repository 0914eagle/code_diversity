
def get_two_suspects(n, p, coders):
    # Initialize a set to store the two suspects
    suspects = set()
    
    # Iterate over the coders
    for coder in coders:
        # If the coder agreed with the choice of the two suspects
        if coder[0] in suspects or coder[1] in suspects:
            # Increment the number of agreed coders
            p -= 1
        
        # If the number of agreed coders is greater than or equal to p
        if p <= 0:
            # Break the loop
            break
    
    # Return the number of possible two-suspect sets
    return len(suspects)

def main():
    # Read the input
    n, p = map(int, input().split())
    coders = [tuple(map(int, input().split())) for _ in range(n)]
    
    # Call the get_two_suspects function
    result = get_two_suspects(n, p, coders)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

