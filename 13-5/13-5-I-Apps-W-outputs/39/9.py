
def f1(n, roads):
    # Initialize a list to store the flipped roads
    flipped_roads = []
    
    # Iterate through each road
    for i in range(n):
        # If the road is not already flipped, flip it
        if i not in flipped_roads:
            flipped_roads.append(i)
    
    # Return the number of flipped roads
    return len(flipped_roads)

def f2(n, roads):
    # Initialize a list to store the flipped roads
    flipped_roads = []
    
    # Iterate through each road
    for i in range(n):
        # If the road is not already flipped, flip it
        if i not in flipped_roads:
            flipped_roads.append(i)
    
    # Return the number of flipped roads
    return len(flipped_roads)

if __name__ == '__main__':
    n = int(input())
    roads = list(map(int, input().split()))
    print(f1(n, roads))
    print(f2(n, roads))

