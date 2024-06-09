
def count_ways(X, N, cars):
    # Initialize a counter for the number of ways
    ways = 0
    
    # Loop over each car
    for car in cars:
        # Get the number of free places in the current car
        free_places = car.count("0")
        
        # Check if the current car has enough free places
        if free_places >= X:
            # Get the number of ways to sell X tickets in the current car
            ways += combinations(free_places, X)
    
    # Return the number of ways
    return ways

def combinations(n, r):
    # Calculate the binomial coefficient
    coeff = 1
    for i in range(n-r+1, n+1):
        coeff *= i
    
    # Calculate the number of combinations
    return coeff // factorial(r)

def factorial(n):
    # Calculate the factorial of n
    result = 1
    for i in range(1, n+1):
        result *= i
    
    # Return the result
    return result

if __name__ == '__main__':
    X, N = map(int, input().split())
    cars = [input() for _ in range(N)]
    print(count_ways(X, N, cars))

