
# Read input
N = int(input())
books = []
for _ in range(N):
    h, t = map(int, input().split())
    books.append((h, t))

# Sort books by height in descending order
books.sort(key=lambda x: x[0], reverse=True)

# Initialize variables for minimum area
min_area = float('inf')

# Iterate through all possible partitions of books
for i in range(1, N-1):
    for j in range(i+1, N):
        shelf1 = books[:i]
        shelf2 = books[i:j]
        shelf3 = books[j:]

        max_height = max(sum([h for h, _ in shelf1]), sum([h for h, _ in shelf2]), sum([h for h, _ in shelf3]))
        max_thickness = max(sum([t for _, t in shelf1]), sum([t for _, t in shelf2]), sum([t for _, t in shelf3]))

        area = max_height * max_thickness
        min_area = min(min_area, area)

# Output the minimum area
print(min_area)
