
def f1(n, q, x_coords, y_coords, zoning_requests):
    # Your code here
    return result

def f2(n, q, x_coords, y_coords, zoning_requests):
    # Your code here
    return result

if __name__ == '__main__':
    n, q = map(int, input().split())
    x_coords = []
    y_coords = []
    zoning_requests = []
    for i in range(n):
        x, y = map(int, input().split())
        x_coords.append(x)
        y_coords.append(y)
    for i in range(q):
        a, b = map(int, input().split())
        zoning_requests.append((a, b))
    result = f1(n, q, x_coords, y_coords, zoning_requests)
    print(result)

