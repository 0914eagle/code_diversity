
def get_maximum_sum(n, m):
    # Initialize the array with all elements as 0
    arr = [0] * n
    
    # Base case: if n is 1, then the only possible array is [m]
    if n == 1:
        return 0
    
    # Initialize the maximum sum to 0
    max_sum = 0
    
    # Iterate over all possible values that the first element of the array can take
    for i in range(m + 1):
        # Recursively find the maximum sum for the remaining elements
        remaining_sum = m - i
        remaining_arr = get_maximum_sum(n - 1, remaining_sum)
        
        # Calculate the sum of absolute differences for the current array
        current_sum = abs(i - remaining_arr[0])
        
        # Update the maximum sum if necessary
        if current_sum > max_sum:
            max_sum = current_sum
    
    return [max_sum] + remaining_arr

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        print(get_maximum_sum(n, m)[0])

if __name__ == "__main__":
    main()

