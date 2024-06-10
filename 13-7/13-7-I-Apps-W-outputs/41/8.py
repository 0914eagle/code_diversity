
def get_moving_cost(requests, teams, locations, costs):
    # Initialize variables
    total_cost = 0
    team_assignment = [0] * len(requests)
    team_location = 1

    # Loop through the requests
    for i in range(len(requests)):
        # Find the team with the lowest cost to move the equipment to the current location
        min_cost = float('inf')
        min_team = 0
        for j in range(teams):
            if costs[team_location][locations[i]] < min_cost:
                min_cost = costs[team_location][locations[i]]
                min_team = j

        # Assign the request to the team and update the team's location
        team_assignment[i] = min_team
        team_location = locations[i]
        total_cost += min_cost

    return total_cost

def main():
    n, k = map(int, input().split())
    requests = [int(input()) for _ in range(n)]
    teams = [int(input()) for _ in range(k)]
    locations = [i for i in range(1, n+1)]
    costs = [[float(input()) for _ in range(n+1)] for _ in range(n+1)]
    print(get_moving_cost(requests, teams, locations, costs))

if __name__ == '__main__':
    main()

