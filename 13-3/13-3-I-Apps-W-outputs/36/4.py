
def get_centroid(n, edges):
    # Your code here
    pass

def get_unique_centroid(n, edges):
    # Your code here
    pass

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        edges = []
        for _ in range(n-1):
            x, y = map(int, input().split())
            edges.append((x, y))
        x1, y1 = get_centroid(n, edges)
        x2, y2 = get_unique_centroid(n, edges)
        print(x1, y1)
        print(x2, y2)

if __name__ == '__main__':
    main()

