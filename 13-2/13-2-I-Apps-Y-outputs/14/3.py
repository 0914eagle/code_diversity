
def solve(n, p, m, names, points):
    # Initialize a dictionary to store the names and points
    name_points = {}
    for i in range(n):
        name_points[names[i]] = 0
    
    # Loop through the points and update the dictionary
    for i in range(m):
        name = points[i][0]
        points_scored = points[i][1]
        name_points[name] += points_scored
    
    # Find the winners
    winners = []
    for name, points in name_points.items():
        if points >= p:
            winners.append(name)
    
    # Print the winners
    if len(winners) == 0:
        print("No winner!")
    else:
        for winner in winners:
            print(f"{winner} wins!")

