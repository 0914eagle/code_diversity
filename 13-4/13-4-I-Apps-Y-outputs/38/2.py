
def get_max_d(x, cities):
    # Sort the cities in ascending order
    sorted_cities = sorted(cities)

    # Initialize the maximum value of D
    max_d = 0

    # Iterate through the cities and calculate the minimum distance between two consecutive cities
    for i in range(len(sorted_cities) - 1):
        d = sorted_cities[i + 1] - sorted_cities[i]
        max_d = max(max_d, d)

    return max_d

def solve(x, cities):
    # Get the maximum value of D that enables you to visit all the cities
    max_d = get_max_d(x, cities)

    # Print the maximum value of D
    print(max_d)

if __name__ == '__main__':
    # Read the input
    n, x = map(int, input().split())
    cities = list(map(int, input().split()))

    # Solve the problem
    solve(x, cities)

