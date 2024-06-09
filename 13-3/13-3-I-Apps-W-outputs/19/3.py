
def f1(S, T, streets, properties):
    # Initialize a dictionary to keep track of the designations for each region
    designations = {}

    # Loop through each street and assign a designation to each region
    for i in range(S):
        # Get the two points that define the street
        point1 = streets[i][0]
        point2 = streets[i][1]

        # Get the x and y coordinates of the points
        x1, y1 = point1
        x2, y2 = point2

        # Determine the region that the street passes through
        region = (x1, y1, x2, y2)

        # Assign a designation to the region
        if region not in designations:
            designations[region] = "residential"
        else:
            designations[region] = "commercial"

    # Loop through each pair of properties and check if they are guaranteed to receive different designations
    for i in range(T):
        # Get the two points that define the property
        point1 = properties[i][0]
        point2 = properties[i][1]

        # Get the x and y coordinates of the points
        x1, y1 = point1
        x2, y2 = point2

        # Determine the regions that the property passes through
        region1 = (x1, y1, x2, y2)
        region2 = (x2, y2, x1, y1)

        # Check if the regions have different designations
        if region1 in designations and region2 in designations and designations[region1] != designations[region2]:
            print("different")
        else:
            print("same")

def f2(...):
    # Implement function 2 here
    pass

if __name__ == '__main__':
    S = int(input())
    T = int(input())
    streets = []
    for i in range(S):
        x1, y1, x2, y2 = map(int, input().split())
        streets.append(((x1, y1), (x2, y2)))
    properties = []
    for i in range(T):
        x1, y1, x2, y2 = map(int, input().split())
        properties.append(((x1, y1), (x2, y2)))
    f1(S, T, streets, properties)

