
def count_ways(n, arr):
    # Base case: if the array has only one element, return 1
    if n == 1:
        return 1
    
    # Initialize the number of ways to break the chocolate to 0
    ways = 0
    
    # Iterate over the array
    for i in range(n):
        # If the current element is 1 (i.e., it contains a nut), check if the previous element is 0 (i.e., it does not contain a nut)
        if arr[i] == 1 and (i == 0 or arr[i-1] == 0):
            # If the previous element is 0, we can break the chocolate after the current element
            ways += count_ways(n-i-1, arr[i+1:])
        # If the current element is 0 (i.e., it does not contain a nut), check if the next element is 1 (i.e., it contains a nut)
        elif arr[i] == 0 and (i == n-1 or arr[i+1] == 1):
            # If the next element is 1, we can break the chocolate before the current element
            ways += count_ways(n-i-1, arr[i+1:])
    
    # Return the number of ways to break the chocolate
    return ways

def main():
    # Read the input n and the array of n integers
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Call the count_ways function and print the result
    print(count_ways(n, arr))

if __name__ == '__main__':
    main()

