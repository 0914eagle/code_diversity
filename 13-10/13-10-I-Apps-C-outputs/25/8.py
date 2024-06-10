
def read_polygon(n):
    polygon = []
    for i in range(n):
        x, y = map(int, input().split())
        polygon.append((x, y))
    return polygon

def find_min_cost(A, B):
    # Implement your solution here
    return 0.0

def main():
    A = read_polygon(int(input()))
    B = read_polygon(int(input()))
    print(find_min_cost(A, B))

if __name__ == '__main__':
    main()

