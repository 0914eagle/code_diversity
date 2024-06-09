
def get_affected_settlements(n, m, d, paths, settlements):
    # Initialize a set to store the affected settlements
    affected_settlements = set()

    # Iterate over the settlements that have been affected by the Book of Evil
    for settlement in settlements:
        # Get the distance between the current settlement and the other settlements
        distances = [get_distance(settlement, other_settlement, paths) for other_settlement in range(1, n + 1)]

        # Check if the current settlement is within the damage range of the Book of Evil
        if any(distance <= d for distance in distances):
            affected_settlements.add(settlement)

    return affected_settlements

def get_distance(settlement, other_settlement, paths):
    # Initialize the distance to infinity
    distance = float('inf')

    # Iterate over the paths to find the shortest distance between the two settlements
    for path in paths:
        if path[0] == settlement and path[1] == other_settlement:
            distance = 1
            break
        elif path[0] == other_settlement and path[1] == settlement:
            distance = 1
            break

    return distance

def main():
    n, m, d = map(int, input().split())
    paths = []
    for _ in range(n - 1):
        paths.append(list(map(int, input().split())))
    settlements = set(map(int, input().split()))
    affected_settlements = get_affected_settlements(n, m, d, paths, settlements)
    print(len(affected_settlements))

if __name__ == '__main__':
    main()

