
def count_ways_to_sell_tickets(X, N, cars):
    # Initialize a counter for the number of ways to sell X tickets
    ways = 0
    
    # Loop over each car
    for car in cars:
        # Get the number of free places in the current car
        free_places = car.count("0")
        
        # Check if the current car has enough free places to sell X tickets
        if free_places >= X:
            # Get the number of ways to sell X tickets in the current car
            ways += combinations(free_places, X)
    
    # Return the number of ways to sell X tickets in total
    return ways

def combinations(n, r):
    # Calculate the number of ways to choose r items from n items
    if r > n:
        return 0
    if r == 0:
        return 1
    if r == n:
        return 1
    else:
        return combinations(n-1, r-1) + combinations(n-1, r)

if __name__ == '__main__':
    X, N = map(int, input().split())
    cars = [input() for _ in range(N)]
    print(count_ways_to_sell_tickets(X, N, cars))

