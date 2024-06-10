
def shots_needed_to_destroy_droids(n, m, k, droids):
    max_shots = [0] * m

    for droid in droids:
        for i in range(m):
            shots = (droid[i] + k - 1) // k
            max_shots[i] = max(max_shots[i], shots)

    return max_shots

if __name__ == "__main__":
    n, m, k = map(int, input().split())
    droids = [list(map(int, input().split())) for _ in range(n)]

    result = shots_needed_to_destroy_droids(n, m, k, droids)
    print(*result)
