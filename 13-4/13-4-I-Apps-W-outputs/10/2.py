
n = int(input())
a = list(map(int, input().split()))

# Initialize a dictionary to store the counts of pairs
pairs = {}

# Iterate over the numbers in the row
for i in range(n):
    # Iterate over the numbers after the current number
    for j in range(i+1, n):
        # If the current number is not equal to the next number, add the pair to the dictionary
        if a[i] != a[j]:
            pairs[(a[i], a[j])] = pairs.get((a[i], a[j]), 0) + 1

# Print the number of possible pairs
print(len(pairs))

