
def get_moving_cost(requests, teams):
    # Initialize variables
    moving_cost = 0
    team_assignment = [0] * len(requests)

    # Loop through the requests and teams
    for i in range(len(requests)):
        for j in range(len(teams)):
            # Check if the request can be served by the current team
            if requests[i] <= teams[j]:
                # Assign the request to the current team
                team_assignment[i] = j + 1
                break

    # Loop through the requests again and calculate the moving cost
    for i in range(1, len(requests)):
        moving_cost += requests[i - 1]

    return moving_cost

def main():
    # Read the input
    n, k = map(int, input().split())
    requests = []
    for i in range(n):
        requests.append(int(input()))

    # Calculate the moving cost
    moving_cost = get_moving_cost(requests, range(1, k + 1))

    # Print the result
    print(moving_cost)

if __name__ == '__main__':
    main()

