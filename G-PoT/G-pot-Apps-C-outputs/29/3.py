
N = int(input())
books = []
for _ in range(N):
    h, t = map(int, input().split())
    books.append((h, t))

books.sort(reverse=True)

min_area = float('inf')
for i in range(1, N-1):
    for j in range(i+1, N):
        shelf1 = sum([h for h, _ in books[:i]])
        shelf2 = sum([h for h, _ in books[i:j]])
        shelf3 = sum([h for h, _ in books[j:]])
        
        max_height = max(shelf1, shelf2, shelf3)
        max_width = max([t for _, t in books])
        
        area = max_height * max_width
        min_area = min(min_area, area)

print(min_area)
