
def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

def get_min_distance(n, a):
    # Sort the list of houses in ascending order
    a.sort()
    # Initialize the minimum distance to 0
    min_distance = 0
    # Iterate through the list of houses
    for i in range(n-1):
        # Calculate the distance between the current house and the next house
        distance = a[i+1] - a[i]
        # If the distance is greater than the minimum distance, update the minimum distance
        if distance > min_distance:
            min_distance = distance
    return min_distance

def main():
    n, a = get_input()
    print(get_min_distance(n, a))

if __name__ == '__main__':
    main()

