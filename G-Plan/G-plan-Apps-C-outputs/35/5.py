
def distribute_sand(n, m, w, h, sand_volumes, dividers, min_sand, max_sand):
    def distribute_section(section, sand_volumes, min_sand, max_sand):
        min_diff = min(max_sand[section] - sand_volumes[section], sand_volumes[section] - min_sand[section])
        sand_volumes[section] = min(max_sand[section], max(min_sand[section], sand_volumes[section]))
        return min_diff

    sand_volumes.sort()
    total_diff = 0
    for i in range(n):
        total_diff += distribute_section(i, sand_volumes, min_sand[i], max_sand[i])

    return round(total_diff / n, 3)

if __name__ == "__main__":
    n, m, w, h = map(int, input().split())
    sand_volumes = list(map(float, input().split()))
    dividers = list(map(float, input().split()))
    min_sand = [list(map(float, input().split())) for _ in range(n)]
    max_sand = [list(map(float, input().split())) for _ in range(n)]

    print(distribute_sand(n, m, w, h, sand_volumes, dividers, min_sand, max_sand))
