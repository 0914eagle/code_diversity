
def get_affected_settlements(n, m, d, paths, affected_settlements):
    # Initialize a set to store the affected settlements
    affected_settlements = set(affected_settlements)

    # Iterate over the paths
    for path in paths:
        # Get the ends of the path
        a, b = path

        # Check if the path connects two affected settlements
        if a in affected_settlements and b in affected_settlements:
            # If the path connects two affected settlements, add the other end of the path to the affected settlements set
            affected_settlements.add(a if a != b else b)

    # Return the number of affected settlements
    return len(affected_settlements)

def main():
    # Read the input
    n, m, d = map(int, input().split())
    affected_settlements = set(map(int, input().split()))
    paths = [tuple(map(int, input().split())) for _ in range(n - 1)]

    # Call the function to get the affected settlements
    affected_settlements = get_affected_settlements(n, m, d, paths, affected_settlements)

    # Print the number of affected settlements
    print(affected_settlements)

if __name__ == '__main__':
    main()

