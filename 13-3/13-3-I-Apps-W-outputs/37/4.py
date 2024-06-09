
def get_highest_and_lowest_place(points_first_round, points_second_round):
    total_points = points_first_round + points_second_round
    if total_points == 0:
        return 1, 1
    else:
        return total_points, total_points

def get_highest_and_lowest_place_list(points_list):
    highest_and_lowest_place_list = []
    for points_first_round, points_second_round in points_list:
        highest_and_lowest_place_list.append(get_highest_and_lowest_place(points_first_round, points_second_round))
    return highest_and_lowest_place_list

if __name__ == '__main__':
    num_contestants = int(input())
    points_list = []
    for _ in range(num_contestants):
        points_first_round, points_second_round = map(int, input().split())
        points_list.append((points_first_round, points_second_round))
    highest_and_lowest_place_list = get_highest_and_lowest_place_list(points_list)
    for highest_and_lowest_place in highest_and_lowest_place_list:
        print(*highest_and_lowest_place)

