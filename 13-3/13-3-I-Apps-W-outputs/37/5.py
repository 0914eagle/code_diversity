
def f1(N, points):
    # Calculate the total points for each contestant
    total_points = [sum(point) for point in points]
    
    # Sort the contestants in descending order of total points
    sorted_indices = sorted(range(len(total_points)), key=lambda i: total_points[i], reverse=True)
    
    # Find the highest and lowest place for each contestant
    highest_place = [i+1 for i in sorted_indices]
    lowest_place = [len(total_points) - i for i in sorted_indices]
    
    return highest_place, lowest_place

def f2(N, points):
    # Calculate the total points for each contestant
    total_points = [sum(point) for point in points]
    
    # Sort the contestants in descending order of total points
    sorted_indices = sorted(range(len(total_points)), key=lambda i: total_points[i], reverse=True)
    
    # Find the highest and lowest place for each contestant
    highest_place = [i+1 for i in sorted_indices]
    lowest_place = [len(total_points) - i for i in sorted_indices]
    
    return highest_place, lowest_place

if __name__ == '__main__':
    N = int(input())
    points = []
    for _ in range(N):
        points.append(list(map(int, input().split())))
    highest_place, lowest_place = f1(N, points)
    for i in range(N):
        print(highest_place[i], lowest_place[i])

