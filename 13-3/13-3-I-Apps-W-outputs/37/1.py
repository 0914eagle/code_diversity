
def f1(N, points):
    # Calculate the total points for each contestant
    total_points = [p1 + p2 for p1, p2 in points]
    
    # Sort the contestants by total points in descending order
    sorted_contestants = sorted(range(N), key=lambda i: total_points[i], reverse=True)
    
    # Find the highest and lowest place for each contestant
    highest_place = 1
    lowest_place = N
    for i in range(N):
        if total_points[sorted_contestants[i]] == total_points[sorted_contestants[0]]:
            highest_place = 1
        else:
            highest_place += 1
        if total_points[sorted_contestants[i]] == total_points[sorted_contestants[-1]]:
            lowest_place = N
        else:
            lowest_place -= 1
    
    return highest_place, lowest_place

def f2(N, points):
    # Calculate the total points for each contestant
    total_points = [p1 + p2 for p1, p2 in points]
    
    # Sort the contestants by total points in descending order
    sorted_contestants = sorted(range(N), key=lambda i: total_points[i], reverse=True)
    
    # Find the highest and lowest place for each contestant
    highest_place = 1
    lowest_place = N
    for i in range(N):
        if total_points[sorted_contestants[i]] == total_points[sorted_contestants[0]]:
            highest_place = 1
        else:
            highest_place += 1
        if total_points[sorted_contestants[i]] == total_points[sorted_contestants[-1]]:
            lowest_place = N
        else:
            lowest_place -= 1
    
    return highest_place, lowest_place

if __name__ == '__main__':
    N = int(input())
    points = []
    for i in range(N):
        p1, p2 = map(int, input().split())
        points.append((p1, p2))
    print(f1(N, points))
    print(f2(N, points))

