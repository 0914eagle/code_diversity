
def get_input():
    N = int(input())
    a = [int(i) for i in input().split()]
    return N, a

def solve(N, a):
    # Sort the list of houses in ascending order
    a.sort()
    # Initialize the minimum distance to be traveled
    min_dist = 0
    # Iterate through the list of houses
    for i in range(N-1):
        # Calculate the distance between the current house and the next house
        dist = a[i+1] - a[i]
        # If the distance is greater than the minimum distance, update the minimum distance
        if dist > min_dist:
            min_dist = dist
    return min_dist

def main():
    N, a = get_input()
    print(solve(N, a))

if __name__ == '__main__':
    main()

