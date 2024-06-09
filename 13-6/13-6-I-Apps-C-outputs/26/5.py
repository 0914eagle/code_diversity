
def read_input():
    n, m, w, h = map(int, input().split())
    assert 2 <= n <= 200 and 1 <= m <= 200 and 1 <= w, h <= 5000
    v = list(map(float, input().split()))
    assert all(0 < v_i <= w*h for v_i in v)
    x = list(map(float, input().split()))
    assert all(0 < x_i < w for x_i in x)
    assert len(x) == n-1 and sorted(x) == x
    min_sand = []
    for i in range(n):
        min_sand.append(list(map(float, input().split())))
    assert all(all(0 <= min_sand_ij <= w*h for min_sand_ij in min_sand_i) for min_sand_i in min_sand)
    max_sand = []
    for i in range(n):
        max_sand.append(list(map(float, input().split())))
    assert all(all(min_sand_ij <= max_sand_ij <= w*h for min_sand_ij, max_sand_ij in zip(min_sand_i, max_sand_i)) for min_sand_i, max_sand_i in zip(min_sand, max_sand))
    return n, m, w, h, v, x, min_sand, max_sand

def f1(n, m, w, h, v, x, min_sand, max_sand):
    # Initialize the variables
    sand = [0] * m
    heights = [0] * n
    for i in range(n):
        heights[i] = 0
    for i in range(m):
        sand[i] = v[i]
    
    # Loop through each section and calculate the height
    for i in range(n):
        for j in range(m):
            if sand[j] > 0:
                if i == 0:
                    heights[i] += sand[j]
                else:
                    heights[i] += min(sand[j], x[i-1] * h)
                sand[j] -= min(sand[j], x[i-1] * h)
    
    # Calculate the minimum and maximum heights
    min_height = min(heights)
    max_height = max(heights)
    
    # Return the difference between the minimum and maximum heights
    return max_height - min_height

def f2(n, m, w, h, v, x, min_sand, max_sand):
    # Initialize the variables
    sand = [0] * m
    heights = [0] * n
    for i in range(n):
        heights[i] = 0
    for i in range(m):
        sand[i] = v[i]
    
    # Loop through each section and calculate the height
    for i in range(n):
        for j in range(m):
            if sand[j] > 0:
                if i == 0:
                    heights[i] += sand[j]
                else:
                    heights[i] += min(sand[j], x[i-1] * h)
                sand[j] -= min(sand[j], x[i-1] * h)
    
    # Calculate the minimum and maximum heights
    min_height = min(heights)
    max_height = max(heights)
    
    # Return the difference between the minimum and maximum heights
    return max_height - min_height

if __name__ == '__main__':
    n, m, w, h, v, x, min_sand, max_sand = read_input()
    print(f1(n, m, w, h, v, x, min_sand, max_sand))
    print(f2(n, m, w, h, v, x, min_sand, max_sand))

