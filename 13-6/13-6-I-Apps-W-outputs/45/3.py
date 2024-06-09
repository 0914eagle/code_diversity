
def count_ways(n, arr):
    # Base case: if there is only one piece, return 1
    if n == 1:
        return 1
    
    # Initialize the number of ways to break the chocolate
    ways = 0
    
    # Iterate over the array of pieces
    for i in range(n):
        # If the current piece has a nut, try breaking the chocolate into two parts
        if arr[i] == 1:
            # Calculate the number of ways to break the chocolate into two parts
            ways += count_ways(i, arr[:i] + arr[i+1:])
    
    return ways

def main():
    # Read the number of pieces and the array of pieces from stdin
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Calculate the number of ways to break the chocolate
    ways = count_ways(n, arr)
    
    # Print the number of ways
    print(ways)

if __name__ == '__main__':
    main()

