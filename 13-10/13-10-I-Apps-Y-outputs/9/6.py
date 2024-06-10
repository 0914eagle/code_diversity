
def is_integer_sold(a, b, x, n):
    # Calculate the price of the integer
    price = a * n + b * len(str(n))
    
    # Check if the price is less than or equal to the given amount
    if price <= x:
        return True
    else:
        return False

def find_largest_integer(a, b, x):
    # Initialize the largest integer found
    largest_integer = 0
    
    # Iterate through the integers from 1 to 10^9
    for i in range(1, 10**9 + 1):
        # Check if the current integer is sold
        if is_integer_sold(a, b, x, i):
            # Update the largest integer found
            largest_integer = i
    
    return largest_integer

def main():
    # Read the input from stdin
    a, b, x = map(int, input().split())
    
    # Find the largest integer that can be bought
    largest_integer = find_largest_integer(a, b, x)
    
    # Print the result
    print(largest_integer)

if __name__ == '__main__':
    main()

