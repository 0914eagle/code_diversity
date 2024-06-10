
def distribute_sand(n, m, w, h, sand_volumes, dividers, min_sand, max_sand):
    sand_volumes.sort()
    total_sand = sum(sand_volumes)
    section_heights = [0] * n
    for i in range(n):
        section_heights[i] = sum(min_sand[i]) / w

    for i in range(n):
        min_height = sum(min_sand[i]) / w
        max_height = sum(max_sand[i]) / w
        for j in range(m):
            target_height = min_height + (max_height - min_height) * sum(min_sand[i][:j+1]) / sum(min_sand[i])
            sand_needed = max(0, target_height - section_heights[i])
            sand_to_add = min(sand_volumes[j], sand_needed)
            section_heights[i] += sand_to_add / w

    return round(max(section_heights) - min(section_heights), 3)

if __name__ == "__main__":
    n, m, w, h = map(int, input().split())
    sand_volumes = list(map(float, input().split()))
    dividers = list(map(float, input().split()))
    min_sand = [list(map(float, input().split())) for _ in range(n)]
    max_sand = [list(map(float, input().split())) for _ in range(n)]

    result = distribute_sand(n, m, w, h, sand_volumes, dividers, min_sand, max_sand)
    print(result)
