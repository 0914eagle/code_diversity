
def get_highest_lowest_place(points1, points2):
    total_points = points1 + points2
    if points1 > points2:
        highest_place = 1
        lowest_place = 3
    else:
        highest_place = 3
        lowest_place = 1
    return highest_place, lowest_place

def main():
    num_contestants = int(input())
    for _ in range(num_contestants):
        points1, points2 = map(int, input().split())
        highest_place, lowest_place = get_highest_lowest_place(points1, points2)
        print(highest_place, lowest_place)

if __name__ == '__main__':
    main()

