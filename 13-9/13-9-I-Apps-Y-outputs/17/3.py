
def get_largest_integer_that_can_be_bought(A, B, X):
    # Initialize a list to store the integers that can be bought
    integers = []
    
    # Loop through the integers from 1 to 10^9
    for i in range(1, 10**9 + 1):
        # Calculate the price of the current integer
        price = A * i + B * len(str(i))
        
        # If the price is less than or equal to X, add the integer to the list
        if price <= X:
            integers.append(i)
    
    # If the list is empty, return 0
    if not integers:
        return 0
    
    # Return the largest integer in the list
    return max(integers)

def main():
    A, B, X = map(int, input().split())
    print(get_largest_integer_that_can_be_bought(A, B, X))

if __name__ == '__main__':
    main()

