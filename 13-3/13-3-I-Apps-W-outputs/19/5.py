
def f1(S, T, streets, properties):
    # Initialize an array to store the designations for each region
    designations = [""] * (S + 1)

    # Loop through each street and determine the regions on either side
    for i in range(S):
        region1 = get_region(streets[i][0], streets[i][1], streets[i][2], streets[i][3])
        region2 = get_region(streets[i][2], streets[i][3], streets[i][0], streets[i][1])
        designations[region1] = "commercial"
        designations[region2] = "residential"

    # Loop through each property and check if the designations are the same
    for i in range(T):
        property1 = properties[i][0]
        property2 = properties[i][1]
        region1 = get_region(property1[0], property1[1], property2[0], property2[1])
        region2 = get_region(property2[0], property2[1], property1[0], property1[1])
        if designations[region1] == designations[region2]:
            return "same"

    return "different"

def get_region(x1, y1, x2, y2):
    # Determine the region based on the slope of the line
    if x1 == x2:
        return x1
    else:
        return x1 + (y1 - y2) // (x1 - x2)

if __name__ == '__main__':
    S = int(input())
    streets = []
    for i in range(S):
        x1, y1, x2, y2 = map(int, input().split())
        streets.append([x1, y1, x2, y2])
    T = int(input())
    properties = []
    for i in range(T):
        x1, y1, x2, y2 = map(int, input().split())
        properties.append([[x1, y1], [x2, y2]])
    print(f1(S, T, streets, properties))

