
def count_ways(x, n, cars):
    # Initialize a counter for the number of ways
    ways = 0
    
    # Loop through each car
    for car in cars:
        # Get the number of free places in the car
        free_places = car.count("0")
        
        # Check if the number of free places is greater than or equal to X
        if free_places >= x:
            # Increment the counter by the number of ways to sell X tickets in the car
            ways += comb(free_places, x)
    
    # Return the number of ways
    return ways

def comb(n, x):
    # Calculate the number of ways to sell X tickets in a compartment with N free places
    if x == 0:
        return 1
    if n == 0:
        return 0
    return comb(n-1, x-1) + comb(n-1, x)

if __name__ == '__main__':
    x, n = map(int, input().split())
    cars = [input() for _ in range(n)]
    print(count_ways(x, n, cars))

