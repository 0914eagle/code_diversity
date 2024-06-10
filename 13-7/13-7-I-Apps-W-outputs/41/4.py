
def get_min_moving_cost(requests, teams):
    # Initialize variables
    min_cost = 0
    team_index = 0
    team_locations = [1]

    # Loop through the requests
    for i in range(len(requests)):
        # Get the current request location and cost
        request_location = i + 2
        request_cost = requests[i]

        # Check if the current team location is the same as the request location
        if team_locations[team_index] == request_location:
            # Add the request cost to the min cost
            min_cost += request_cost
        else:
            # Calculate the distance between the current team location and the request location
            distance = abs(team_locations[team_index] - request_location)

            # Check if the distance is greater than the number of teams
            if distance > teams:
                # Add the request cost to the min cost
                min_cost += request_cost
            else:
                # Calculate the cost of moving the team to the request location
                move_cost = requests[team_index + distance]

                # Check if the move cost is less than the request cost
                if move_cost < request_cost:
                    # Add the move cost to the min cost
                    min_cost += move_cost
                else:
                    # Add the request cost to the min cost
                    min_cost += request_cost

                # Update the team location
                team_locations.append(request_location)
                team_index += 1

    return min_cost

def main():
    # Read the number of requests and teams
    n, k = map(int, input().split())

    # Read the requests
    requests = []
    for i in range(n):
        requests.append(int(input()))

    # Get the minimum moving cost
    min_cost = get_min_moving_cost(requests, k)

    # Print the minimum moving cost
    print(min_cost)

if __name__ == '__main__':
    main()

