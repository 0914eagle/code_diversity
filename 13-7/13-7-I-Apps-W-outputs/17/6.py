
def get_lost_potatoes(y, k, n):
    # Initialize an empty list to store the possible values of x
    possible_x = []
    
    # Iterate from 1 to n
    for x in range(1, n + 1):
        # Check if x + y is divisible by k
        if (x + y) % k == 0:
            # Add x to the list of possible values of x
            possible_x.append(x)
    
    # Return the list of possible values of x
    return possible_x

def main():
    # Accept input y, k, and n from stdin
    y, k, n = map(int, input().split())
    
    # Call the get_lost_potatoes function and store the result in possible_x
    possible_x = get_lost_potatoes(y, k, n)
    
    # Check if possible_x is empty
    if not possible_x:
        # If it is empty, print -1
        print(-1)
    else:
        # If it is not empty, sort possible_x in ascending order and print it
        print(*sorted(possible_x), sep=' ')

if __name__ == '__main__':
    main()

