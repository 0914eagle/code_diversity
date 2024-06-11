
def distribute_sand(n, m, w, h, sand_volumes, dividers, min_sand, max_sand):
    sand_volumes.sort()
    sections = [0] * n
    for i in range(n):
        for j in range(m):
            min_amount = min_sand[i][j]
            max_amount = max_sand[i][j]
            amount = min(sand_volumes[j], max_amount)
            sections[i] += amount
            sand_volumes[j] -= amount
    min_height = min(sections)
    max_height = max(sections)
    return round((max_height - min_height) / h, 3)

if __name__ == "__main__":
    n, m, w, h = map(int, input().split())
    sand_volumes = list(map(float, input().split()))
    dividers = list(map(float, input().split()))
    min_sand = [list(map(float, input().split())) for _ in range(n)]
    max_sand = [list(map(float, input().split())) for _ in range(n)]

    result = distribute_sand(n, m, w, h, sand_volumes, dividers, min_sand, max_sand)
    print(result)