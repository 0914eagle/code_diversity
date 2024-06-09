
def read_input():
    n_r, n_c, n, m = map(int, input().split())
    assert 1 <= n_r <= 10000 and 1 <= n_c <= 10000 and 1 <= n + m <= 100
    files = []
    for _ in range(n + m):
        r, c = map(int, input().split())
        assert 0 <= r < n_r and 0 <= c < n_c
        files.append((r, c))
    return n_r, n_c, n, m, files

def get_rectangle(files):
    rows, cols = zip(*files)
    top_row, bottom_row = min(rows), max(rows)
    left_col, right_col = min(cols), max(cols)
    return top_row, bottom_row, left_col, right_col

def get_rectangle_area(top_row, bottom_row, left_col, right_col):
    return (bottom_row - top_row + 1) * (right_col - left_col + 1)

def get_distance(file1, file2):
    return abs(file1[0] - file2[0]) + abs(file1[1] - file2[1])

def get_closest_pair(files):
    min_distance = float('inf')
    closest_pair = []
    for i in range(len(files)):
        for j in range(i + 1, len(files)):
            distance = get_distance(files[i], files[j])
            if distance < min_distance:
                min_distance = distance
                closest_pair = [i, j]
    return closest_pair

def solve(n_r, n_c, n, m, files):
    rectangle = get_rectangle(files)
    rectangle_area = get_rectangle_area(*rectangle)
    closest_pair = get_closest_pair(files)
    distance = get_distance(files[closest_pair[0]], files[closest_pair[1]])
    return max(rectangle_area, distance)

def main():
    n_r, n_c, n, m, files = read_input()
    print(solve(n_r, n_c, n, m, files))

if __name__ == '__main__':
    main()

