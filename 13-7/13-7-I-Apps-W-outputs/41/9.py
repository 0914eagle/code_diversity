
def get_moving_cost(requests, teams, costs):
    # Initialize variables
    total_cost = 0
    current_location = 1
    teams_assigned = 0

    # Iterate through the requests
    for request in requests:
        # Calculate the distance between the current location and the request location
        distance = abs(request - current_location)

        # If the distance is greater than the number of teams available, assign a team to the request
        if distance > teams_assigned:
            total_cost += costs[current_location][request]
            current_location = request
            teams_assigned += 1

    # Return the total cost
    return total_cost

def main():
    # Read the input
    n, k = map(int, input().split())
    requests = [int(x) for x in input().split()]
    costs = []
    for i in range(n):
        costs.append([int(x) for x in input().split()])

    # Call the get_moving_cost function
    total_cost = get_moving_cost(requests, k, costs)

    # Print the result
    print(total_cost)

if __name__ == '__main__':
    main()

