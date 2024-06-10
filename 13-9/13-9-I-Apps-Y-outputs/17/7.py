
def get_largest_integer(A, B, X):
    # Initialize variables
    largest_integer = 0
    current_integer = 1
    current_price = A * current_integer + B * len(str(current_integer))
    
    # Loop through the integers and find the largest that can be bought
    while current_price <= X:
        largest_integer = current_integer
        current_integer += 1
        current_price = A * current_integer + B * len(str(current_integer))
    
    # Return the largest integer that can be bought
    return largest_integer

def main():
    # Read input from stdin
    A, B, X = map(int, input().split())
    
    # Call the get_largest_integer function and print the result
    largest_integer = get_largest_integer(A, B, X)
    print(largest_integer)

if __name__ == '__main__':
    main()

