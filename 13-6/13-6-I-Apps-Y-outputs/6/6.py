
def get_input():
    N = int(input())
    a = list(map(int, input().split()))
    return N, a

def get_min_distance(a):
    # Sort the list of coordinates in ascending order
    a.sort()
    # Initialize the minimum distance to be traveled
    min_distance = 0
    # Iterate through the list of coordinates
    for i in range(len(a)):
        # Calculate the distance traveled from the current coordinate to the next coordinate
        distance = a[i+1] - a[i]
        # If the distance is greater than the minimum distance, update the minimum distance
        if distance > min_distance:
            min_distance = distance
    return min_distance

def main():
    N, a = get_input()
    print(get_min_distance(a))

if __name__ == '__main__':
    main()

