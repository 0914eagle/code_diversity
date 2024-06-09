
def f1(n, x1, y1, x2, y2, *coords):
    # Calculate the distances between the fountains and the flowers
    dist_1 = [(x - x1) ** 2 + (y - y1) ** 2 for x, y in coords]
    dist_2 = [(x - x2) ** 2 + (y - y2) ** 2 for x, y in coords]
    
    # Find the minimum value of r_1^2 + r_2^2 that covers all flowers
    min_val = float('inf')
    for r1 in range(1, int(max(dist_1)) + 1):
        r2 = int(max(dist_2))
        while r2 * r2 < min_val:
            r2 += 1
        min_val = min(min_val, r1 * r1 + r2 * r2)
    
    return min_val

