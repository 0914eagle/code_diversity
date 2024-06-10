
def distribute_sand(n, m, w, h, sand_volumes, dividers, min_sand, max_sand):
    def calculate_heights(sand_distribution):
        heights = [0] * n
        for i in range(n):
            for j in range(m):
                heights[i] += sand_distribution[i][j]
        return heights

    def calculate_difference(heights):
        return max(heights) - min(heights)

    def distribute_greedy(sand_volumes, min_sand, max_sand):
        sand_distribution = [[0] * m for _ in range(n)]
        sorted_colors = sorted(range(m), key=lambda x: sand_volumes[x])
        
        for color in sorted_colors:
            for i in range(n):
                for j in range(m):
                    if sand_volumes[color] > 0 and min_sand[i][color] > 0:
                        amount = min(sand_volumes[color], min_sand[i][color])
                        sand_distribution[i][color] += amount
                        sand_volumes[color] -= amount
                        min_sand[i][color] -= amount
        
        return sand_distribution

    sand_distribution = distribute_greedy(sand_volumes.copy(), min_sand.copy(), max_sand.copy())
    heights = calculate_heights(sand_distribution)
    return round(calculate_difference(heights) / h, 3)

if __name__ == "__main__":
    n, m, w, h = map(int, input().split())
    sand_volumes = list(map(float, input().split()))
    dividers = list(map(float, input().split()))
    min_sand = [list(map(float, input().split())) for _ in range(n)]
    max_sand = [list(map(float, input().split())) for _ in range(n)]

    result = distribute_sand(n, m, w, h, sand_volumes, dividers, min_sand, max_sand)
    print(result)
