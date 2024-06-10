
def read_input():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        x_coords = list(map(int, input().split()))
        y_coords = list(map(int, input().split()))
        yield n, k, x_coords, y_coords

def place_platforms(n, k, x_coords, y_coords):
    # find the left and right borders of the platforms
    left_border = min(x_coords)
    right_border = max(x_coords) + k
    
    # count the number of points that are on the platforms
    num_points = 0
    for i in range(n):
        if left_border <= x_coords[i] <= right_border:
            num_points += 1
    
    return num_points

def solve(n, k, x_coords, y_coords):
    # find the maximum number of points that can be saved by placing the platforms optimally
    max_num_points = 0
    for i in range(n):
        for j in range(i+1, n):
            # check if the platforms overlap
            if x_coords[i] <= x_coords[j] <= x_coords[i] + k:
                continue
            # count the number of points that are on both platforms
            num_points = place_platforms(n, k, x_coords[i:j+1], y_coords[i:j+1])
            max_num_points = max(max_num_points, num_points)
    
    return max_num_points

def main():
    for n, k, x_coords, y_coords in read_input():
        print(solve(n, k, x_coords, y_coords))

if __name__ == '__main__':
    main()

