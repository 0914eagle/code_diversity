
def count_ways(X, N, cars):
    # Initialize a counter for the number of ways to sell X tickets
    ways = 0
    
    # Iterate over each car
    for car in cars:
        # Initialize a counter for the number of free places in the current car
        free_places = 0
        
        # Iterate over each compartment in the current car
        for compartment in range(9):
            # Iterate over each place in the current compartment
            for place in range(6):
                # Check if the current place is free
                if car[compartment * 6 + place] == '0':
                    # Increment the counter for the number of free places in the current car
                    free_places += 1
                    
        # Check if the current car has at least X free places
        if free_places >= X:
            # Increment the counter for the number of ways to sell X tickets
            ways += 1
    
    # Return the number of ways to sell X tickets
    return ways

def main():
    X, N = map(int, input().split())
    cars = [input() for _ in range(N)]
    print(count_ways(X, N, cars))

if __name__ == '__main__':
    main()

