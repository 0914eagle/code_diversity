
def f1(S, T, streets, properties):
    # Initialize a dictionary to store the designations for each region
    designations = {}

    # Iterate over the streets
    for i in range(S):
        # Get the two points that define the current street
        point1 = streets[i][0]
        point2 = streets[i][1]

        # Get the region that the current street divides the town into
        region = get_region(point1, point2)

        # Add the region to the dictionary with the corresponding designation
        designations[region] = "commercial" if i % 2 == 0 else "residential"

    # Iterate over the pairs of properties to be tested
    for i in range(T):
        # Get the two points that define the current property
        point1 = properties[i][0]
        point2 = properties[i][1]

        # Get the regions that the current property divides the town into
        region1 = get_region(point1, point2)
        region2 = get_region(point2, point1)

        # Check if the regions have different designations
        if designations[region1] != designations[region2]:
            print("different")
        else:
            print("same")

def get_region(point1, point2):
    # Get the x and y coordinates of the two points
    x1, y1 = point1
    x2, y2 = point2

    # Get the slope of the line that passes through the two points
    slope = (y2 - y1) / (x2 - x1)

    # Get the region that the line divides the town into
    if slope < 0:
        return "top"
    elif slope > 0:
        return "bottom"
    else:
        return "left" if x1 < x2 else "right"

if __name__ == '__main__':
    S, T = map(int, input().split())
    streets = []
    for i in range(S):
        x1, y1, x2, y2 = map(int, input().split())
        streets.append(((x1, y1), (x2, y2)))
    properties = []
    for i in range(T):
        x1, y1, x2, y2 = map(int, input().split())
        properties.append(((x1, y1), (x2, y2)))
    f1(S, T, streets, properties)

