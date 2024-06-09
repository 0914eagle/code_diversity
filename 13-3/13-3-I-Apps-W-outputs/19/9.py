
def f1(S, T, streets, properties):
    # Initialize a dictionary to store the designations for each region
    designations = {}

    # Iterate over the streets
    for i in range(S):
        # Get the two points that define the current street
        point1 = streets[i][0]
        point2 = streets[i][1]

        # Determine the region that the current street divides the town into
        region = (point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2

        # If the region has not been assigned a designation yet, assign it "residential"
        if region not in designations:
            designations[region] = "residential"

    # Iterate over the properties
    for i in range(T):
        # Get the two points that define the current property
        point1 = properties[i][0]
        point2 = properties[i][1]

        # Determine the region that the current property is located in
        region = (point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2

        # If the region has not been assigned a designation yet, assign it "commercial"
        if region not in designations:
            designations[region] = "commercial"

    # Iterate over the properties again
    for i in range(T):
        # Get the two points that define the current property
        point1 = properties[i][0]
        point2 = properties[i][1]

        # Determine the region that the current property is located in
        region = (point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2

        # If the region has been assigned a designation, check if it is the same as the designation of the other property
        if region in designations:
            if designations[region] == designations[(point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2]:
                return "same"

    return "different"

def f2(...):
    # Implement function f2 here
    pass

if __name__ == '__main__':
    S = int(input())
    T = int(input())
    streets = []
    for i in range(S):
        x1, y1, x2, y2 = map(int, input().split())
        streets.append([(x1, y1), (x2, y2)])
    properties = []
    for i in range(T):
        x3, y3, x4, y4 = map(int, input().split())
        properties.append([(x3, y3), (x4, y4)])
    print(f1(S, T, streets, properties))

