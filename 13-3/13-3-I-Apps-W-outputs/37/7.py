
def get_ranking(points1, points2):
    # Calculate the total points for each contestant
    total_points = points1 + points2
    
    # Sort the contestants in descending order based on their total points
    ranking = sorted(range(len(total_points)), key=lambda k: total_points[k], reverse=True)
    
    return ranking

def get_highest_lowest_place(ranking, n):
    # Get the highest and lowest place for the nth contestant
    highest_place = ranking.index(n) + 1
    lowest_place = len(ranking) - ranking[::-1].index(n)
    
    return highest_place, lowest_place

def main():
    # Read the number of contestants and their points from stdin
    num_contestants = int(input())
    points1 = []
    points2 = []
    for _ in range(num_contestants):
        points1.append(int(input()))
        points2.append(int(input()))
    
    # Get the ranking of the contestants
    ranking = get_ranking(points1, points2)
    
    # Print the highest and lowest place for each contestant
    for i in range(num_contestants):
        highest_place, lowest_place = get_highest_lowest_place(ranking, i)
        print(highest_place, lowest_place)

if __name__ == '__main__':
    main()

