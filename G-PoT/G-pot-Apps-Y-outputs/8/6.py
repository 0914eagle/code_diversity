
q = int(input())
for _ in range(q):
    l1, r1, l2, r2 = map(int, input().split())
    a = l1
    b = l2 + 1 if l2 != l1 else l2
    print(a, b)
    