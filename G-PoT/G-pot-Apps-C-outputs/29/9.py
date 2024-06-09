
N = int(input())
books = []
for _ in range(N):
    h, t = map(int, input().split())
    books.append((h, t))

books.sort(reverse=True)

min_area = float('inf')
for i in range(1, N-1):
    for j in range(i+1, N):
        h1 = sum(h for h, _ in books[:i])
        h2 = sum(h for h, _ in books[i:j])
        h3 = sum(h for h, _ in books[j:])
        t1 = max(t for _, t in books[:i])
        t2 = max(t for _, t in books[i:j])
        t3 = max(t for _, t in books[j:])
        area = max(h1, h2, h3) * (t1 + t2 + t3)
        min_area = min(min_area, area)

print(min_area)
