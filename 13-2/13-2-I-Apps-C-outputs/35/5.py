
def max_operations(arr, pairs):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize a variable to store the maximum number of operations
    max_ops = 0
    # Iterate over the good pairs
    for i, j in pairs:
        # Check if the sum of the indices is odd
        if i + j % 2 == 1:
            # Find the greatest common divisor of the two elements
            gcd = find_gcd(arr[i - 1], arr[j - 1])
            # Check if the gcd is greater than 1
            if gcd > 1:
                # Divide both elements by the gcd
                arr[i - 1] //= gcd
                arr[j - 1] //= gcd
                # Increment the maximum number of operations
                max_ops += 1
    # Return the maximum number of operations
    return max_ops

def find_gcd(a, b):
    if b == 0:
        return a
    else:
        return find_gcd(b, a % b)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
pairs = []
for i in range(m):
    i, j = map(int, input().split())
    pairs.append((i, j))
print(max_operations(arr, pairs))

