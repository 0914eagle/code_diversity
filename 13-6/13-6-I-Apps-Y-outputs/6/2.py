
def get_min_distance(a):
    # Sort the list of coordinates in ascending order
    a.sort()
    # Initialize the minimum distance to 0
    min_distance = 0
    # Loop through the list of coordinates
    for i in range(len(a)-1):
        # Calculate the distance between the current coordinate and the next coordinate
        distance = a[i+1] - a[i]
        # If the distance is greater than the minimum distance, update the minimum distance
        if distance > min_distance:
            min_distance = distance
    # Return the minimum distance
    return min_distance

def main():
    # Read the number of houses and the coordinates of the houses from stdin
    n = int(input())
    a = list(map(int, input().split()))
    # Call the get_min_distance function and print the result
    print(get_min_distance(a))

if __name__ == '__main__':
    main()

