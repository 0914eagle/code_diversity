
def count_ways(n, a):
    # Base case: if n is 1, there is only one way to break the chocolate
    if n == 1:
        return 1
    
    # Initialize the number of ways to break the chocolate
    ways = 0
    
    # Iterate over all possible breaks
    for i in range(n - 1):
        # If the current piece contains a nut
        if a[i] == 1:
            # Count the number of ways to break the chocolate after the current piece
            ways += count_ways(n - i - 1, a[i + 1:])
    
    return ways

def main():
    # Read the input
    n = int(input())
    a = list(map(int, input().split()))
    
    # Calculate the number of ways to break the chocolate
    ways = count_ways(n, a)
    
    # Print the result
    print(ways)

if __name__ == '__main__':
    main()

