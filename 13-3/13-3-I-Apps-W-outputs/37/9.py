
def get_ranking_range(points_1st_round, points_2nd_round):
    total_points = points_1st_round + points_2nd_round
    if total_points == 0:
        return (1, 1)
    elif total_points == 650:
        return (1, 1)
    else:
        return (total_points // 151 + 1, total_points // 151 + 1)

def get_ranking_range_after_3rd_round(points_1st_round, points_2nd_round, points_3rd_round):
    total_points = points_1st_round + points_2nd_round + points_3rd_round
    if total_points == 0:
        return (1, 1)
    elif total_points == 650:
        return (1, 1)
    else:
        return (total_points // 151 + 1, total_points // 151 + 1)

def main():
    num_contestants = int(input())
    for _ in range(num_contestants):
        points_1st_round, points_2nd_round = map(int, input().split())
        print(*get_ranking_range(points_1st_round, points_2nd_round))

if __name__ == '__main__':
    main()

