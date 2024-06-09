
def get_input():
    n, m, w, h = map(int, input().split())
    volumes = list(map(float, input().split()))
    x_coords = list(map(float, input().split()))
    min_sand = [[0] * m for _ in range(n)]
    max_sand = [[0] * m for _ in range(n)]
    for i in range(n):
        min_sand[i] = list(map(float, input().split()))
        max_sand[i] = list(map(float, input().split()))
    return n, m, w, h, volumes, x_coords, min_sand, max_sand

def get_possible_distributions(n, m, w, h, volumes, x_coords, min_sand, max_sand):
    possible_distributions = []
    for i in range(n):
        for j in range(m):
            min_volume = min_sand[i][j] * w * h
            max_volume = max_sand[i][j] * w * h
            possible_distributions.append((i, j, min_volume, max_volume))
    return possible_distributions

def get_min_max_heights(possible_distributions, n, m, w, h, volumes, x_coords):
    min_heights = [0] * n
    max_heights = [0] * n
    for i in range(n):
        for j in range(m):
            min_volume = possible_distributions[i * m + j][2]
            max_volume = possible_distributions[i * m + j][3]
            min_heights[i] += min(min_volume, volumes[j])
            max_heights[i] += max(max_volume, volumes[j])
    return min_heights, max_heights

def get_min_diff(min_heights, max_heights):
    min_diff = float('inf')
    for i in range(len(min_heights)):
        for j in range(i+1, len(min_heights)):
            diff = abs(min_heights[i] - min_heights[j])
            if diff < min_diff:
                min_diff = diff
    return min_diff

def solve(n, m, w, h, volumes, x_coords, min_sand, max_sand):
    possible_distributions = get_possible_distributions(n, m, w, h, volumes, x_coords, min_sand, max_sand)
    min_heights, max_heights = get_min_max_heights(possible_distributions, n, m, w, h, volumes, x_coords)
    return get_min_diff(min_heights, max_heights)

if __name__ == '__main__':
    n, m, w, h, volumes, x_coords, min_sand, max_sand = get_input()
    print(f'{solve(n, m, w, h, volumes, x_coords, min_sand, max_sand):.3f}')

