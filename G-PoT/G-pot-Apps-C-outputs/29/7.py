
# Read input
N = int(input())
books = []
for _ in range(N):
    h, t = map(int, input().split())
    books.append((h, t))

# Sort books by height in descending order
books.sort(key=lambda x: x[0], reverse=True)

# Initialize variables for minimum area calculation
min_area = float('inf')

# Iterate through all possible partitions of books into three sets
for i in range(1, N-1):
    for j in range(i+1, N):
        set1 = books[:i]
        set2 = books[i:j]
        set3 = books[j:]

        max_height = max(sum(h for h, _ in set1), sum(h for h, _ in set2), sum(h for h, _ in set3))
        max_thickness = max(sum(t for _, t in set1), sum(t for _, t in set2), sum(t for _, t in set3))

        area = max_height * max_thickness
        min_area = min(min_area, area)

# Output the minimum area
print(min_area)
