
def get_highest_and_lowest_place(points1, points2):
    total_points = points1 + points2
    if points1 > points2:
        highest_place = 1
        lowest_place = 3
    elif points1 < points2:
        highest_place = 3
        lowest_place = 1
    else:
        highest_place = 1
        lowest_place = 1
    return highest_place, lowest_place

def get_ranking_list(contestants):
    ranking_list = []
    for contestant in contestants:
        points1, points2 = contestant
        highest_place, lowest_place = get_highest_and_lowest_place(points1, points2)
        ranking_list.append((highest_place, lowest_place))
    return ranking_list

def get_total_ranking_list(ranking_list):
    total_ranking_list = []
    for ranking in ranking_list:
        highest_place, lowest_place = ranking
        total_ranking_list.append((highest_place, lowest_place))
    return total_ranking_list

def get_highest_and_lowest_place_for_each_contestant(contestants):
    ranking_list = get_ranking_list(contestants)
    total_ranking_list = get_total_ranking_list(ranking_list)
    highest_and_lowest_place_for_each_contestant = []
    for ranking in total_ranking_list:
        highest_place, lowest_place = ranking
        highest_and_lowest_place_for_each_contestant.append((highest_place, lowest_place))
    return highest_and_lowest_place_for_each_contestant

if __name__ == '__main__':
    num_contestants = int(input())
    contestants = []
    for _ in range(num_contestants):
        points1, points2 = map(int, input().split())
        contestants.append((points1, points2))
    highest_and_lowest_place_for_each_contestant = get_highest_and_lowest_place_for_each_contestant(contestants)
    for highest_place, lowest_place in highest_and_lowest_place_for_each_contestant:
        print(highest_place, lowest_place)

