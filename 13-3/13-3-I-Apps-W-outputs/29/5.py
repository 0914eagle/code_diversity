
def f1(n, x1, y1, x2, y2, *coords):
    # Calculate the distances between the fountains and the flowers
    dist1 = [(x1-x)**2 + (y1-y)**2 for x, y in coords]
    dist2 = [(x2-x)**2 + (y2-y)**2 for x, y in coords]
    
    # Find the minimum value of r1^2 + r2^2 that covers all the flowers
    r1 = min(dist1) ** 0.5
    r2 = min(dist2) ** 0.5
    return r1**2 + r2**2

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    n, x1, y1, x2, y2 = map(int, input().split())
    coords = [tuple(map(int, input().split())) for _ in range(n)]
    print(f1(n, x1, y1, x2, y2, *coords))

