
n, m, k = map(int, input().split())
p = list(map(int, input().split()))

# Initialize a list to store the number of operations for each page
operations = [0] * (n // k + 1)

# Iterate through the special items to be discarded
for i in range(m):
    # Get the index of the special item
    index = p[i]
    
    # Get the page number of the special item
    page = index // k
    
    # Increment the number of operations for the page
    operations[page] += 1

# Iterate through the pages
for i in range(n // k + 1):
    # If the page has special items, update the number of operations
    if operations[i] > 0:
        operations[i] += 1
    
    # If the page has no special items, update the number of operations for the next page
    else:
        operations[i + 1] += 1

# Print the total number of operations
print(sum(operations))

