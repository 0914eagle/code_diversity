
import math

def solve(n, m, stations):
    # Initialize the probability of meeting at each station
    probabilities = [0] * n
    probabilities[stations[0]] = 1
    probabilities[stations[1]] = 1

    # Iterate through each minute
    for minute in range(2, n * n):
        # Find the current station of Alice and Bob
        current_station_alice = stations[0]
        current_station_bob = stations[1]

        # If they are at the same station, they meet
        if current_station_alice == current_station_bob:
            return minute

        # Otherwise, they take a train to a neighboring station
        neighboring_stations = get_neighboring_stations(current_station_alice, current_station_bob, n, m, stations)
        next_station_alice = neighboring_stations[0]
        next_station_bob = neighboring_stations[1]

        # Update the probability of meeting at each station
        probabilities[next_station_alice] += probabilities[current_station_alice] / 2
        probabilities[next_station_bob] += probabilities[current_station_bob] / 2
        probabilities[current_station_alice] = 0
        probabilities[current_station_bob] = 0

        # Update the current station of Alice and Bob
        stations[0] = next_station_alice
        stations[1] = next_station_bob

    # If they never meet, return "never meet"
    return "never meet"

def get_neighboring_stations(current_station_alice, current_station_bob, n, m, stations):
    # Find the neighbors of the current station of Alice and Bob
    neighbors_alice = get_neighbors(current_station_alice, n, m, stations)
    neighbors_bob = get_neighbors(current_station_bob, n, m, stations)

    # Choose a neighboring station for Alice and Bob uniformly at random
    next_station_alice = neighbors_alice[int(math.floor(random.random() * len(neighbors_alice)))]
    next_station_bob = neighbors_bob[int(math.floor(random.random() * len(neighbors_bob)))]

    return [next_station_alice, next_station_bob]

def get_neighbors(current_station, n, m, stations):
    # Find the neighbors of the current station
    neighbors = []
    for i in range(m):
        if stations[i][0] == current_station or stations[i][1] == current_station:
            if stations[i][0] != current_station:
                neighbors.append(stations[i][0])
            if stations[i][1] != current_station:
                neighbors.append(stations[i][1])

    return neighbors

if __name__ == "__main__":
    n, m = map(int, input().split())
    stations = []
    for i in range(m):
        stations.append(list(map(int, input().split())))
    s, t = map(int, input().split())
    print(solve(n, m, stations))

