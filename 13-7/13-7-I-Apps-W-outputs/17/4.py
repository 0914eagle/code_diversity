
def get_lost_potatoes(y, k, n):
    # Initialize an empty list to store the possible values of x
    x_list = []
    
    # Iterate from 1 to n
    for x in range(1, n + 1):
        # Check if x + y is divisible by k
        if (x + y) % k == 0:
            # Add x to the list of possible values of x
            x_list.append(x)
    
    # Sort the list of possible values of x in ascending order
    x_list.sort()
    
    # Return the list of possible values of x
    return x_list

def main():
    # Read the input data
    y, k, n = map(int, input().split())
    
    # Call the get_lost_potatoes function and store the result in a variable
    x_list = get_lost_potatoes(y, k, n)
    
    # Check if the list is empty
    if len(x_list) == 0:
        # If the list is empty, print -1
        print(-1)
    else:
        # If the list is not empty, print the list of possible values of x in ascending order
        for x in x_list:
            print(x, end=" ")

if __name__ == '__main__':
    main()

