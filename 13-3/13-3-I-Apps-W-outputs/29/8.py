
def f1(n, x1, y1, x2, y2, *coords):
    # Calculate the distances between the fountains and the flowers
    dist1 = [(x1-x)**2 + (y1-y)**2 for x, y in coords]
    dist2 = [(x2-x)**2 + (y2-y)**2 for x, y in coords]
    
    # Find the minimum value of r1^2 + r2^2 that covers all flowers
    r1 = int(max(dist1))
    r2 = int(max(dist2))
    return r1**2 + r2**2

def f2(n, x1, y1, x2, y2, *coords):
    # Calculate the distances between the fountains and the flowers
    dist1 = [(x1-x)**2 + (y1-y)**2 for x, y in coords]
    dist2 = [(x2-x)**2 + (y2-y)**2 for x, y in coords]
    
    # Find the minimum value of r1^2 + r2^2 that covers all flowers
    r1 = int(max(dist1))
    r2 = int(max(dist2))
    return r1**2 + r2**2

if __name__ == '__main__':
    n, x1, y1, x2, y2 = map(int, input().split())
    coords = [(int(x), int(y)) for x, y in zip(*[iter(input().split())] * 2)]
    print(f1(n, x1, y1, x2, y2, *coords))
    print(f2(n, x1, y1, x2, y2, *coords))

