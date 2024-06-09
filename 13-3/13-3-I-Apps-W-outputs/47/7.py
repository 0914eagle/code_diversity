
def count_ways(X, N, cars):
    # Initialize a counter for the number of ways
    ways = 0
    
    # Loop through each car
    for car in cars:
        # Get the number of free places in the car
        free_places = car.count("0")
        
        # Check if the number of free places is greater than or equal to X
        if free_places >= X:
            # Get the number of ways to sell X tickets in the car
            ways += combination(free_places, X)
    
    # Return the number of ways
    return ways

def combination(n, r):
    # Calculate the combination using the formula: n! / (n-r)! * r!
    return factorial(n) // (factorial(n-r) * factorial(r))

def factorial(n):
    # Calculate the factorial of n using the formula: n! = n * (n-1) * (n-2) * ... * 1
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

if __name__ == '__main__':
    X, N = map(int, input().split())
    cars = [input() for _ in range(N)]
    print(count_ways(X, N, cars))

