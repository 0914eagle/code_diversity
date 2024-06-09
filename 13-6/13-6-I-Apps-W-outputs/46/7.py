
def solve(n, a):
    # Count the number of occurrences of each color
    count = [0] * 21
    for i in a:
        count[i] += 1
    
    # Find the leftmost and rightmost position of each color
    left = [0] * 21
    right = [0] * 21
    for i in range(1, 21):
        if count[i] > 0:
            left[i] = a.index(i) + 1
            right[i] = left[i] + count[i] - 1
    
    # Calculate the minimum number of operations
    operations = 0
    for i in range(1, 21):
        if count[i] > 1:
            operations += count[i] - 1
    
    return operations

