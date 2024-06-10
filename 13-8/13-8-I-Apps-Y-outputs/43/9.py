
def get_good_observatories(n, m, heights, roads):
    # Initialize a dictionary to store the height of each observatory
    observatory_heights = {i: heights[i-1] for i in range(1, n+1)}
    # Initialize a set to store the good observatories
    good_observatories = set()
    
    for i in range(m):
        # Get the two observatories connected by the current road
        observatory1 = roads[i][0]
        observatory2 = roads[i][1]
        # If the elevation of the first observatory is higher than the second observatory, add the first observatory to the set of good observatories
        if observatory_heights[observatory1] > observatory_heights[observatory2]:
            good_observatories.add(observatory1)
        # If the elevation of the second observatory is higher than the first observatory, add the second observatory to the set of good observatories
        elif observatory_heights[observatory2] > observatory_heights[observatory1]:
            good_observatories.add(observatory2)
    
    return len(good_observatories)

def main():
    n, m = map(int, input().split())
    heights = list(map(int, input().split()))
    roads = [list(map(int, input().split())) for _ in range(m)]
    print(get_good_observatories(n, m, heights, roads))

if __name__ == '__main__':
    main()

