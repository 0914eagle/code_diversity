
def get_min_distance(n, x1, y1, x2, y2, flowers):
    # Calculate the distance between the fountains and the flowers
    dist_1 = [(abs(x1-x) + abs(y1-y)) for x, y in flowers]
    dist_2 = [(abs(x2-x) + abs(y2-y)) for x, y in flowers]
    
    # Find the minimum distance between the fountains and the flowers
    min_dist_1 = min(dist_1)
    min_dist_2 = min(dist_2)
    
    # Calculate the minimum possible value of r1 and r2
    r1 = int(min_dist_1 ** 0.5)
    r2 = int(min_dist_2 ** 0.5)
    
    # Calculate the sum of the squares of r1 and r2
    sum_squares = r1**2 + r2**2
    
    return sum_squares

def main():
    n, x1, y1, x2, y2 = map(int, input().split())
    flowers = []
    for _ in range(n):
        x, y = map(int, input().split())
        flowers.append((x, y))
    print(get_min_distance(n, x1, y1, x2, y2, flowers))

if __name__ == '__main__':
    main()

