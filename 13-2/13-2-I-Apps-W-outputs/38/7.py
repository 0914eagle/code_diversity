
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        result = 0
        while i > 0:
            result += self.tree[i]
            i -= i & -i
        return result

n, q = map(int, input().split())
ft = FenwickTree(n)
for _ in range(q):
    op, i, delta = input().split()
    if op == "+":
        ft.update(int(i), int(delta))
    else:
        print(ft.query(int(i)))

