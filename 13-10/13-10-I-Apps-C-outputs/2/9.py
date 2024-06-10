
import sys

class UnionFind:
    def __init__(self, n):
        self.parents = [-1] * n
        self.sizes = [1] * n

    def find(self, a):
        if self.parents[a] < 0:
            return a
        else:
            self.parents[a] = self.find(self.parents[a])
            return self.parents[a]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a != b:
            if self.sizes[a] < self.sizes[b]:
                self.parents[a] = b
                self.sizes[b] += self.sizes[a]
            else:
                self.parents[b] = a
                self.sizes[a] += self.sizes[b]

def parse_input():
    n, q = map(int, input().split())
    queries = []
    for _ in range(q):
        queries.append(input().split())
    return n, q, queries

def run_queries(n, queries):
    union_find = UnionFind(n)
    for query in queries:
        if query[0] == "?":
            a, b = map(int, query[1:])
            if union_find.find(a) == union_find.find(b):
                print("yes")
            else:
                print("no")
        else:
            a, b = map(int, query[1:])
            union_find.union(a, b)

if __name__ == '__main__':
    n, q, queries = parse_input()
    run_queries(n, queries)

