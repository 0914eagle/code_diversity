
def get_min_cost(points_a, points_b):
    # Calculate the total length of polygon A
    total_length_a = 0
    for i in range(len(points_a)):
        current_point = points_a[i]
        next_point = points_a[(i + 1) % len(points_a)]
        total_length_a += (next_point[0] - current_point[0]) ** 2 + (next_point[1] - current_point[1]) ** 2

    # Calculate the total length of polygon B
    total_length_b = 0
    for i in range(len(points_b)):
        current_point = points_b[i]
        next_point = points_b[(i + 1) % len(points_b)]
        total_length_b += (next_point[0] - current_point[0]) ** 2 + (next_point[1] - current_point[1]) ** 2

    # Calculate the minimum cost by comparing the total length of polygon A and polygon B
    return total_length_a - total_length_b

def main():
    # Read the input
    num_points_a = int(input())
    points_a = []
    for i in range(num_points_a):
        x, y = map(int, input().split())
        points_a.append((x, y))
    num_points_b = int(input())
    points_b = []
    for i in range(num_points_b):
        x, y = map(int, input().split())
        points_b.append((x, y))

    # Calculate the minimum cost
    min_cost = get_min_cost(points_a, points_b)

    # Print the minimum cost
    print(min_cost)

if __name__ == '__main__':
    main()

