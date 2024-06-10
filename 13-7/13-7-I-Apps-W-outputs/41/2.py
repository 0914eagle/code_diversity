
def get_min_moving_cost(requests, teams, moving_costs):
    # Initialize the minimum moving cost to 0
    min_cost = 0
    # Initialize the current location to 1
    current_location = 1
    # Initialize the current team to 1
    current_team = 1
    # Loop through the requests
    for request in requests:
        # Calculate the cost of moving the equipment to the request location
        cost = moving_costs[current_location - 1][request - current_location]
        # If the cost is less than or equal to the current team's capacity, move the equipment to the request location
        if cost <= teams[current_team - 1]:
            min_cost += cost
            current_location = request
        # Otherwise, move the equipment to the next team's location
        else:
            min_cost += teams[current_team - 1]
            current_team += 1
            current_location = request
    return min_cost

def main():
    # Read the number of requests and teams
    n, k = map(int, input().split())
    # Read the moving costs
    moving_costs = []
    for i in range(n):
        moving_costs.append(list(map(int, input().split())))
    # Read the teams' capacities
    teams = list(map(int, input().split()))
    # Calculate the minimum moving cost
    min_cost = get_min_moving_cost(range(1, n + 1), teams, moving_costs)
    # Print the minimum moving cost
    print(min_cost)

if __name__ == '__main__':
    main()

