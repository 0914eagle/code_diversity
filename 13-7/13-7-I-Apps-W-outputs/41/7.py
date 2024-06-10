
def get_moving_cost(requests, teams, locations):
    # Initialize variables
    total_cost = 0
    team_assignments = []
    team_locations = [1] * teams

    # Loop through the requests
    for i, request in enumerate(requests):
        # Find the team with the least distance to the request location
        team_index = team_locations.index(min(team_locations))
        team_location = team_locations[team_index]
        team_locations[team_index] = request[0]

        # Add the cost of moving the team to the request location
        total_cost += locations[team_location][request[0]]

        # Assign the team to the request
        team_assignments.append((team_index, request[0]))

    # Return the total cost and the team assignments
    return total_cost, team_assignments

def main():
    # Read the input
    n, k = map(int, input().split())
    requests = [list(map(int, input().split())) for _ in range(n)]
    locations = [[0] * (n+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(i+1, n+1):
            locations[i][j] = int(input())

    # Get the minimum moving cost and team assignments
    total_cost, team_assignments = get_moving_cost(requests, k, locations)

    # Print the output
    print(total_cost)

if __name__ == '__main__':
    main()

