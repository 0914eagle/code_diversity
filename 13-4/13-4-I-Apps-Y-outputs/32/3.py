
def get_min_value(n, k):
    # Initialize the minimum value to be displayed on the board
    min_value = 1
    
    # Iterate through the number of operations
    for i in range(n):
        # If the current value is even, double it
        if min_value % 2 == 0:
            min_value *= 2
        # If the current value is odd, add K to it
        else:
            min_value += k
    
    # Return the minimum value displayed on the board after N operations
    return min_value

def main():
    # Read the number of operations and the value of K from stdin
    n, k = map(int, input().split())
    
    # Call the get_min_value function and print the result
    print(get_min_value(n, k))

if __name__ == '__main__':
    main()

