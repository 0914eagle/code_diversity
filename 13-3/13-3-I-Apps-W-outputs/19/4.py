
def f1(S, T, streets, properties):
    # Initialize a dictionary to store the designations for each region
    designations = {}

    # Loop through each street
    for i in range(S):
        # Get the two points that define the street
        point1 = streets[i][0]
        point2 = streets[i][1]

        # Get the region that the street passes through
        region = get_region(point1, point2)

        # If the region is not already in the dictionary, add it with a value of "residential"
        if region not in designations:
            designations[region] = "residential"

        # If the region is already in the dictionary, check if the current designation is the same as the previous one
        else:
            if designations[region] == "residential":
                designations[region] = "commercial"

    # Loop through each property
    for i in range(T):
        # Get the two points that define the property
        point1 = properties[i][0]
        point2 = properties[i][1]

        # Get the region that the property is in
        region = get_region(point1, point2)

        # If the region is not already in the dictionary, add it with a value of "residential"
        if region not in designations:
            designations[region] = "residential"

        # If the region is already in the dictionary, check if the current designation is the same as the previous one
        else:
            if designations[region] == "residential":
                print("different")
            else:
                print("same")

def get_region(point1, point2):
    # Get the x and y coordinates of the two points
    x1, y1 = point1
    x2, y2 = point2

    # Get the region that the line passes through
    region = (x1, y1, x2, y2)

    return region

if __name__ == '__main__':
    S = int(input())
    streets = []
    for i in range(S):
        x1, y1, x2, y2 = map(int, input().split())
        streets.append(((x1, y1), (x2, y2)))
    T = int(input())
    properties = []
    for i in range(T):
        x1, y1, x2, y2 = map(int, input().split())
        properties.append(((x1, y1), (x2, y2)))
    f1(S, T, streets, properties)

