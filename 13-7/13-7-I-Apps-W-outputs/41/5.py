
def get_min_moving_cost(requests, teams, move_costs):
    # Initialize variables
    min_cost = 0
    team_assignment = [0] * len(requests)
    team_costs = [0] * teams

    # Sort requests by event time
    requests.sort(key=lambda x: x[0])

    # Loop through requests
    for i in range(len(requests)):
        # Find the team with the lowest cost
        min_team = 0
        for j in range(1, teams):
            if team_costs[j] < team_costs[min_team]:
                min_team = j

        # Assign the request to the team with the lowest cost
        team_assignment[i] = min_team
        team_costs[min_team] += move_costs[requests[i][0] - 1][min_team]

        # Update the minimum cost
        if team_costs[min_team] < min_cost:
            min_cost = team_costs[min_team]

    return min_cost

def main():
    n, k = map(int, input().split())
    requests = []
    for i in range(n):
        requests.append(list(map(int, input().split())))
    move_costs = [[0] * k for _ in range(n)]
    for i in range(n):
        for j in range(1, n - i):
            move_costs[i][j] = int(input())
    print(get_min_moving_cost(requests, k, move_costs))

if __name__ == '__main__':
    main()

