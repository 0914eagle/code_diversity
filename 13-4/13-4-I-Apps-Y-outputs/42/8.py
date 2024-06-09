
n = int(input())
a = list(map(int, input().split()))

# Initialize a dictionary to store the number of immediate subordinates for each member
subordinates = {i: 0 for i in range(1, n + 1)}

# Iterate over the input and increment the number of immediate subordinates for each member
for i in range(2, n + 1):
    subordinates[a[i - 1]] += 1

# Print the number of immediate subordinates for each member
for i in range(1, n + 1):
    print(subordinates[i])

