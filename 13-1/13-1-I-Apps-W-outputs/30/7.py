
def solve(s):
    # Initialize variables
    min_length = float('inf')
    compressed_version = ''

    # Iterate through all possible combinations of characters and their counts
    for i in range(1, len(s)):
        for j in range(1, len(s) // i + 1):
            # If the current combination results in a shorter compressed version, update the minimum length and the compressed version
            if len(compress(s, i, j)) < min_length:
                min_length = len(compress(s, i, j))
                compressed_version = compress(s, i, j)

    # Return the minimum length
    return min_length

# Compress a string by repeating each character a certain number of times
def compress(s, i, j):
    return str(i) + s[0] * j + compress(s[1:], i, j) if s else ''

