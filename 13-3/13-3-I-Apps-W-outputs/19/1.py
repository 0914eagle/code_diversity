
def f1(S, T, streets, properties):
    # Initialize a dictionary to store the designations for each region
    designations = {}

    # Loop through each street and determine the regions on either side of the street
    for street in streets:
        region1 = (street[0], street[1])
        region2 = (street[2], street[3])

        # If the regions have not been assigned a designation yet, assign one of "residential" or "commercial"
        if region1 not in designations:
            designations[region1] = "residential" if len(designations) % 2 == 0 else "commercial"
        if region2 not in designations:
            designations[region2] = "residential" if len(designations) % 2 == 0 else "commercial"

        # If the regions on either side of the street have different designations, assign the other designation to the region in between
        if designations[region1] != designations[region2]:
            designations[(region1[0] + region2[0]) // 2, (region1[1] + region2[1]) // 2] = designations[region1] if designations[region1] == "residential" else "commercial"

    # Loop through each property and determine its designation based on the region it is in
    for property in properties:
        region = (property[0], property[1])
        if region in designations:
            print(designations[region])
        else:
            print("same")

def f2(...):
    ...

if __name__ == '__main__':
    S = int(input())
    T = int(input())
    streets = []
    for _ in range(S):
        x1, y1, x2, y2 = map(int, input().split())
        streets.append((x1, y1, x2, y2))
    properties = []
    for _ in range(T):
        x3, y3, x4, y4 = map(int, input().split())
        properties.append((x3, y3, x4, y4))
    f1(S, T, streets, properties)

