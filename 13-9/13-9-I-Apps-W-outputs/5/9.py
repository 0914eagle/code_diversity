
def solve(lanterns, length):
    # Sort the lanterns by their positions
    lanterns.sort()
    
    # Initialize the minimum light radius to be the maximum distance between any two lanterns
    min_radius = max(lanterns[-1] - lanterns[0], length - lanterns[-1] + lanterns[0])
    
    # Iterate over the lanterns and calculate the distance between each pair of lanterns
    for i in range(len(lanterns) - 1):
        distance = lanterns[i + 1] - lanterns[i]
        if distance < min_radius:
            min_radius = distance
    
    return min_radius

