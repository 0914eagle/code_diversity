
def distribute_sand(n, m, w, h, sand_volumes, dividers, min_sand, max_sand):
    sand_volumes.sort()
    sand_levels = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            sand_levels[i][j] = min(max(min_sand[i][j], sand_volumes[j]), max_sand[i][j])
    
    section_heights = [0] * n
    for i in range(n):
        section_heights[i] = sum(sand_levels[i])
    
    min_height = min(section_heights)
    max_height = max(section_heights)
    
    return round((max_height - min_height) / h, 3)

if __name__ == "__main__":
    n, m, w, h = map(int, input().split())
    sand_volumes = list(map(float, input().split()))
    dividers = list(map(float, input().split()))
    
    min_sand = []
    max_sand = []
    for _ in range(n):
        min_sand.append(list(map(float, input().split())))
    for _ in range(n):
        max_sand.append(list(map(float, input().split()))
    
    result = distribute_sand(n, m, w, h, sand_volumes, dividers, min_sand, max_sand)
    print(result)
