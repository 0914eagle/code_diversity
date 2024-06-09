
def get_ranking(contestants):
    # Sort the contestants in descending order based on the sum of points from all three rounds
    contestants.sort(key=lambda x: x[0] + x[1], reverse=True)
    
    # Initialize the ranking list with the first place
    ranking = [1]
    
    # Iterate through the contestants and assign the appropriate place based on the sum of points
    for i in range(1, len(contestants)):
        if contestants[i][0] + contestants[i][1] == contestants[i-1][0] + contestants[i-1][1]:
            ranking.append(ranking[i-1])
        else:
            ranking.append(ranking[i-1] + 1)
    
    return ranking

def get_highest_lowest_place(contestants, ranking):
    highest_place = []
    lowest_place = []
    
    for i in range(len(contestants)):
        highest_place.append(ranking[i])
        lowest_place.append(ranking[i])
    
    return highest_place, lowest_place

def main():
    num_contestants = int(input())
    contestants = []
    
    for i in range(num_contestants):
        points1, points2 = map(int, input().split())
        contestants.append((points1, points2))
    
    ranking = get_ranking(contestants)
    highest_place, lowest_place = get_highest_lowest_place(contestants, ranking)
    
    for i in range(num_contestants):
        print(highest_place[i], lowest_place[i])

if __name__ == '__main__':
    main()

