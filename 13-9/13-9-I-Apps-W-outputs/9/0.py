
def get_max_distance(n, x, a, b):
    if a == b:
        return 0
    
    dist = abs(a - b)
    if x == 0:
        return dist
    
    # Find the minimum distance between a and b
    min_dist = min(dist, n - dist + 1)
    
    # If we can do at most x swaps, we can only move them by at most x positions
    max_dist = min_dist + x
    
    return max_dist

def main():
    t = int(input())
    for _ in range(t):
        n, x, a, b = map(int, input().split())
        print(get_max_distance(n, x, a, b))

if __name__ == '__main__':
    main()

