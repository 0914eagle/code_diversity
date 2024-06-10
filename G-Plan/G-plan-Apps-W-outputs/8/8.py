
def max_shots_to_destroy_droids(n, m, k, droids):
    max_shots = [0] * m
    
    for droid in droids:
        for i in range(m):
            shots_needed = max(0, droid[i] - k)
            max_shots[i] = max(max_shots[i], shots_needed)
    
    return max_shots

if __name__ == "__main__":
    n, m, k = map(int, input().split())
    droids = [list(map(int, input().split())) for _ in range(n)]
    
    result = max_shots_to_destroy_droids(n, m, k, droids)
    print(*result)
