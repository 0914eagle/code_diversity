
def get_highest_lowest_place(points_first_round, points_second_round):
    total_points = points_first_round + points_second_round
    if total_points == 0:
        return 1, 1
    highest_place = 1
    for i in range(1, N):
        if total_points > points[i][0] + points[i][1]:
            highest_place += 1
    lowest_place = highest_place
    for i in range(N-1, -1, -1):
        if total_points < points[i][0] + points[i][1]:
            lowest_place -= 1
    return highest_place, lowest_place

def main():
    global N
    N = int(input())
    points = []
    for i in range(N):
        points.append(list(map(int, input().split())))
    for i in range(N):
        print(get_highest_lowest_place(points[i][0], points[i][1]))

if __name__ == '__main__':
    main()

