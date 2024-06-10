t_sets(n, points):
    counts = {}
    for x, y in points:
        if y not in counts:
            counts[y] = 1
        else:
            counts[y] += 1

    result = 1
    for count in counts.values():
        result *= count + 1

    return result

if __name__ == "__main__":
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    print(count_sets(n, points))
