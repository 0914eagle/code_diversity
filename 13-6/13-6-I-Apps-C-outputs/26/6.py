
def get_min_max_heights(sand_heights):
    return min(sand_heights), max(sand_heights)

def get_min_diff(min_heights, max_heights):
    return abs(max_heights - min_heights)

def solve(n, m, w, h, volumes, x_coords, min_sand_reqs, max_sand_reqs):
    total_volume = sum(volumes)
    total_sand = total_volume * h
    section_volume = total_volume / n
    section_sand = total_sand / n
    section_heights = [section_sand / w for _ in range(n)]
    min_heights = [0 for _ in range(n)]
    max_heights = [0 for _ in range(n)]
    for i in range(n):
        min_heights[i] = min_sand_reqs[i] / section_sand
        max_heights[i] = max_sand_reqs[i] / section_sand
    min_diff = get_min_diff(min_heights, max_heights)
    for i in range(n):
        for j in range(m):
            if min_heights[i] > section_heights[i]:
                min_heights[i] = section_heights[i]
            if max_heights[i] < section_heights[i]:
                max_heights[i] = section_heights[i]
    min_diff = get_min_diff(min_heights, max_heights)
    return min_diff

if __name__ == '__main__':
    n, m, w, h = map(int, input().split())
    volumes = list(map(float, input().split()))
    x_coords = list(map(float, input().split()))
    min_sand_reqs = [list(map(float, input().split())) for _ in range(n)]
    max_sand_reqs = [list(map(float, input().split())) for _ in range(n)]
    print(solve(n, m, w, h, volumes, x_coords, min_sand_reqs, max_sand_reqs))

