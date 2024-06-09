
n = int(input())
a = list(map(int, input().split()))

# Initialize a set to store the pairs
pairs = set()

# Loop through each number in the list
for i in range(n):
    # Loop through each number after the current number
    for j in range(i+1, n):
        # If the current number is less than the next number, add the pair to the set
        if a[i] < a[j]:
            pairs.add((a[i], a[j]))

# Print the length of the set
print(len(pairs))

