
def get_lifelines(edges):
    lifelines = set()
    for edge in edges:
        lifelines.add(frozenset(edge))
    return len(lifelines)

def main():
    n = int(input())
    edges = []
    for _ in range(n - 1):
        edges.append(tuple(map(int, input().split())))
    print(get_lifelines(edges))

if __name__ == '__main__':
    main()

