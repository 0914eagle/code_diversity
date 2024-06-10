
def distribute_sand(n, m, w, h, sand_volumes, dividers, min_sand, max_sand):
    sand_volumes.sort()
    section_heights = [0] * n
    for i in range(n):
        for j in range(m):
            min_amount = min_sand[i][j]
            max_amount = max_sand[i][j]
            diff = min(max_amount, sand_volumes[j]) - min_amount
            section_heights[i] += diff / w
            sand_volumes[j] -= diff
    return round(max(section_heights) - min(section_heights), 3)

if __name__ == "__main__":
    n, m, w, h = map(int, input().split())
    sand_volumes = list(map(float, input().split()))
    dividers = list(map(float, input().split()))
    min_sand = [list(map(float, input().split())) for _ in range(n)]
    max_sand = [list(map(float, input().split())) for _ in range(n)]
    
    result = distribute_sand(n, m, w, h, sand_volumes, dividers, min_sand, max_sand)
    print(result)
