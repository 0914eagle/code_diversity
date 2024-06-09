
def get_min_cost(flights, additional_flights):
    # Initialize a dictionary to store the minimum cost for each airport
    min_cost = {1: 0}
    for airport in range(2, len(flights) + 1):
        min_cost[airport] = float('inf')

    # Loop through all the flights and calculate the minimum cost for each airport
    for flight in flights:
        cost = flight[2]
        airport1, airport2 = flight[0], flight[1]
        min_cost[airport2] = min(min_cost[airport2], min_cost[airport1] + cost)

    # Loop through all the additional flights and calculate the minimum cost for each airport
    for flight in additional_flights:
        cost = flight[2]
        airport1, airport2 = flight[0], flight[1]
        min_cost[airport2] = min(min_cost[airport2], min_cost[airport1] + cost)

    # Return the minimum cost for airport 1, which is the total cost of the flights
    return min_cost[1]

def main():
    # Read the input data
    num_airports, num_flights = map(int, input().split())
    flights = []
    for _ in range(num_flights):
        flights.append(list(map(int, input().split())))
    num_additional_flights = int(input())
    additional_flights = []
    for _ in range(num_additional_flights):
        additional_flights.append(list(map(int, input().split())))

    # Calculate the minimum cost and print the output
    min_cost = get_min_cost(flights, additional_flights)
    print(min_cost)

if __name__ == '__main__':
    main()

