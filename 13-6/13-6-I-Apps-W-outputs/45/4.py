
def get_number_of_ways(n, a):
    # Initialize the number of ways to 0
    number_of_ways = 0
    
    # Loop through all possible breaks
    for i in range(n):
        # Check if the current break is valid
        if a[i] == 1:
            # Increment the number of ways
            number_of_ways += 1
    
    # Return the number of ways
    return number_of_ways

def main():
    # Read the input
    n = int(input())
    a = list(map(int, input().split()))
    
    # Calculate the number of ways
    number_of_ways = get_number_of_ways(n, a)
    
    # Print the result
    print(number_of_ways)

if __name__ == '__main__':
    main()

