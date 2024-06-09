
def read_data():
    n, m = map(int, input().split())
    edges = []
    for i in range(n - 1):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    queries = list(map(int, input().split()))
    return n, m, edges, queries

def f1(n, m, edges, queries):
    # Implement your solution here
    return [0] * m

def f2(n, m, edges, queries):
    # Implement your solution here
    return [0] * m

def main():
    n, m, edges, queries = read_data()
    answers = [0] * m
    for i in range(m):
        answers[i] = f1(n, m, edges, queries[i])
    print(*answers, sep='\n')

if __name__ == '__main__':
    main()

