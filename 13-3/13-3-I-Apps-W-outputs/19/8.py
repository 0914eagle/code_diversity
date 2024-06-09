
def f1(S, T, streets, properties):
    # Initialize a dictionary to store the designations for each region
    designations = {}

    # Loop through each street and determine the regions on either side of the street
    for street in streets:
        region1 = (street[0], street[1])
        region2 = (street[2], street[3])

        # If the region1 is not in the dictionary, add it with a random designation
        if region1 not in designations:
            designations[region1] = "residential" if random.random() < 0.5 else "commercial"

        # If the region2 is not in the dictionary, add it with the opposite designation of region1
        if region2 not in designations:
            designations[region2] = "residential" if designations[region1] == "commercial" else "commercial"

    # Loop through each property and determine if it is guaranteed to receive the same or different designation
    for property in properties:
        region = (property[0], property[1])
        if region in designations:
            yield "same"
        else:
            yield "different"

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
    for result in f1(S, T, streets, properties):
        print(result)

