
def solve(points, k):
    # Sort the points by their x-coordinates
    points.sort(key=lambda x: x[0])
    
    # Initialize the maximum number of points that can be saved
    max_points = 0
    
    # Loop through all possible starting points for the first platform
    for i in range(len(points)):
        # Initialize the number of points that can be saved for this platform
        points_saved = 0
        
        # Loop through all possible ending points for the first platform
        for j in range(i, len(points)):
            # Check if the platform overlaps with any other platform
            overlaps = False
            for platform in platforms:
                if platform[0] <= points[j][0] <= platform[1] or platform[0] <= points[i][0] <= platform[1]:
                    overlaps = True
                    break
            
            # If the platform does not overlap with any other platform, increment the number of points that can be saved
            if not overlaps:
                points_saved += 1
            
            # If the platform is long enough, add it to the list of platforms
            if points[j][0] - points[i][0] + 1 >= k:
                platforms.append([points[i][0], points[j][0]])
        
        # Update the maximum number of points that can be saved
        max_points = max(max_points, points_saved)
    
    return max_points

def read_input():
    # Read the number of test cases
    t = int(input())
    
    # Loop through each test case
    for _ in range(t):
        # Read the number of points and the length of each platform
        n, k = map(int, input().split())
        
        # Read the x-coordinates of the points
        x = [int(x) for x in input().split()]
        
        # Read the y-coordinates of the points
        y = [int(y) for y in input().split()]
        
        # Create a list of points
        points = [(x[i], y[i]) for i in range(n)]
        
        # Find the maximum number of points that can be saved
        max_points = solve(points, k)
        
        # Print the answer for this test case
        print(max_points)

if __name__ == '__main__':
    read_input()

