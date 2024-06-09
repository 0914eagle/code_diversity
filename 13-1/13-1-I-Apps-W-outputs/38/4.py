
n = int(input())
a = list(map(int, input().split()))

# Use a dictionary to count the frequency of each number in the sequence
freq = {}
for num in a:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

# Find all numbers that occur more than once in the sequence
valid_x = []
for x, count in freq.items():
    if count > 1:
        valid_x.append(x)

# Sort the valid x values in increasing order
valid_x.sort()

# Print the number of valid x values
print(len(valid_x))

# Print the valid x values and their common differences
for x in valid_x:
    # Find the positions of x in the sequence
    positions = [i for i, num in enumerate(a) if num == x]
    # Sort the positions in increasing order
    positions.sort()
    # Calculate the common difference between the positions
    common_diff = positions[1] - positions[0]
    print(x, common_diff)

