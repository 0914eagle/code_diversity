
def count_ways_to_sell_tickets(X, N, cars):
    # Initialize a counter for the number of ways to sell X tickets
    ways = 0
    
    # Iterate over each car
    for car in cars:
        # Initialize a counter for the number of free places in the current car
        free_places = 0
        
        # Iterate over each place in the current car
        for place in car:
            # If the place is free, increment the counter for free places
            if place == "0":
                free_places += 1
        
        # If the number of free places is divisible by X, increment the counter for the number of ways to sell X tickets
        if free_places % X == 0:
            ways += 1
    
    # Return the number of ways to sell X tickets
    return ways

def main():
    X, N = map(int, input().split())
    cars = [input() for _ in range(N)]
    print(count_ways_to_sell_tickets(X, N, cars))

if __name__ == '__main__':
    main()

