
# Read input
n = int(input())
trees = list(map(int, input().split()))

# Sort the trees in descending order of growth time
trees.sort(reverse=True)

# Calculate the earliest day when the party can be organized
earliest_day = max(trees[i] + i + 1 for i in range(n))

# Output the result
print(earliest_day)
