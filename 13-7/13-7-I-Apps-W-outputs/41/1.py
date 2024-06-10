
def get_min_moving_cost(n, k, requests):
    # Initialize a list to store the minimum moving cost for each request
    min_costs = [0] * n
    # Initialize a list to store the available teams
    available_teams = list(range(k))
    # Loop through the requests
    for i in range(n):
        # Get the cost of moving the equipment from the current location to the next location
        cost = requests[i][0]
        # If the cost is 0, it means the equipment is already at the correct location, so skip this request
        if cost == 0:
            continue
        # Find the team that is closest to the current location
        min_index = 0
        for j in range(1, k):
            if requests[i][j] < requests[i][min_index]:
                min_index = j
        # Remove the team from the available teams list
        available_teams.remove(min_index)
        # Add the cost to the minimum moving cost for this request
        min_costs[i] += cost
        # If there are no more available teams, break the loop
        if not available_teams:
            break
    # Return the sum of the minimum moving costs
    return sum(min_costs)

def main():
    n, k = map(int, input().split())
    requests = []
    for i in range(n):
        requests.append(list(map(int, input().split())))
    print(get_min_moving_cost(n, k, requests))

if __name__ == '__main__':
    main()

