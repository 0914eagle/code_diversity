
def count_ways(n, k, S, a):
    # Base case: if S is 0, there is only one way to choose no cubes and stick no exclamation marks
    if S == 0:
        return 1
    
    # Initialize the number of ways to choose some cubes and stick exclamation marks as 0
    ways = 0
    
    # Iterate over the cubes
    for i in range(n):
        # If the current cube has a number that is less than or equal to S, we can choose it
        if a[i] <= S:
            # Recursively call the function to count the number of ways to choose the remaining cubes and stick exclamation marks
            ways += count_ways(n-1, k-1, S-a[i], a[i+1:])
    
    # Return the number of ways to choose some cubes and stick exclamation marks
    return ways

def main():
    # Read the input
    n, k, S = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Call the count_ways function to count the number of ways to choose some cubes and stick exclamation marks
    ways = count_ways(n, k, S, a)
    
    # Print the number of ways
    print(ways)

if __name__ == '__main__':
    main()

