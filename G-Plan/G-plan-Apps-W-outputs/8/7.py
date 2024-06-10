ulate_shots_needed(droids, m, k):
    max_shots = [0] * m
    for droid in droids:
        for i in range(m):
            shots_needed = (droid[i] + k - 1) // k
            max_shots[i] = max(max_shots[i], shots_needed)
    return max_shots

if __name__ == "__main__":
    n, m, k = map(int, input().split())
    droids = [list(map(int, input().split())) for _ in range(n)]
    result = calculate_shots_needed(droids, m, k)
    print(*result)  
