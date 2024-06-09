
def find_affected_settlements(n, m, d, paths, affected_settlements):
    # Initialize a set to store the affected settlements
    affected_settlements = set(affected_settlements)

    # Iterate over the paths
    for path in paths:
        # Get the ends of the path
        a, b = path

        # Check if the path connects two affected settlements
        if a in affected_settlements and b in affected_settlements:
            # If the path connects two affected settlements, add the other settlements in the range of d to the affected settlements set
            for i in range(1, d + 1):
                affected_settlements.add(a + i)
                affected_settlements.add(b + i)

    # Return the number of affected settlements
    return len(affected_settlements)

def main():
    # Read the input
    n, m, d = map(int, input().split())
    affected_settlements = set(map(int, input().split()))
    paths = []
    for _ in range(n - 1):
        a, b = map(int, input().split())
        paths.append((a, b))

    # Find the affected settlements
    affected_settlements = find_affected_settlements(n, m, d, paths, affected_settlements)

    # Print the number of affected settlements
    print(affected_settlements)

if __name__ == '__main__':
    main()

