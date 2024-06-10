
def get_moving_cost(moving_costs, requests):
    # Initialize variables
    total_cost = 0
    current_location = 1
    team_assignments = [[] for _ in range(k)]

    # Loop through the requests
    for request in requests:
        # Find the closest team with available equipment
        closest_team = -1
        for i in range(k):
            if len(team_assignments[i]) < requests[i]:
                closest_team = i
                break

        # If there are no available teams, move the equipment to the current location
        if closest_team == -1:
            total_cost += moving_costs[current_location][request[0]]
            current_location = request[0]
        else:
            # Assign the request to the closest team
            team_assignments[closest_team].append(request)

    # Return the total cost
    return total_cost

def main():
    # Read the input
    n, k = map(int, input().split())
    moving_costs = []
    for i in range(n):
        moving_costs.append(list(map(int, input().split())))
    requests = []
    for i in range(n):
        requests.append(int(input()))

    # Calculate the minimum moving cost
    minimum_cost = get_moving_cost(moving_costs, requests)

    # Print the result
    print(minimum_cost)

if __name__ == '__main__':
    main()

