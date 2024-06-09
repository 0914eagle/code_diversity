
def solve(n, arr):
    # Initialize a dictionary to store the count of each number
    count = {}
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    # Initialize the minimum number of operations to 0
    min_ops = 0
    
    # Loop through the dictionary and find the maximum number of operations required to delete all occurrences of each number
    for num, count in count.items():
        min_ops += count // (num + 1)
    
    return min_ops

