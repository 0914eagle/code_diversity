
def distribute_sand(n, m, w, h, sand_volumes, dividers, min_sand, max_sand):
    sand_volumes.sort()
    sand_distribution = [[0 for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            sand_distribution[i][j] = min(max(min_sand[i][j], sand_volumes[j]), max_sand[i][j])
    
    max_height = [0] * n
    min_height = [float('inf')] * n
    
    for i in range(n):
        for j in range(m):
            max_height[i] = max(max_height[i], sand_distribution[i][j])
            min_height[i] = min(min_height[i], sand_distribution[i][j])
    
    return round(max(max_height) - min(min_height), 3)

if __name__ == "__main__":
    n, m, w, h = map(int, input().split())
    sand_volumes = list(map(float, input().split()))
    dividers = list(map(float, input().split()))
    
    min_sand = []
    max_sand = []
    
    for _ in range(n):
        min_sand.append(list(map(float, input().split())))
    
    for _ in range(n):
        max_sand.append(list(map(float, input().split())))
    
    result = distribute_sand(n, m, w, h, sand_volumes, dividers, min_sand, max_sand)
    print(result)
