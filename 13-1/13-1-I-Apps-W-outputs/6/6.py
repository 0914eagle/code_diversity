
def get_max_total_significance(n, m, d, physics_cups, informatics_cups):
    # Sort the cups by their significance in descending order
    physics_cups.sort(key=lambda x: x[0], reverse=True)
    informatics_cups.sort(key=lambda x: x[0], reverse=True)

    # Initialize the variables to keep track of the exposed cups and the total significance
    exposed_physics_cups = 0
    exposed_informatics_cups = 0
    total_significance = 0

    # Loop through the cups and expose them on the shelf
    while exposed_physics_cups < n and exposed_informatics_cups < m:
        # Expose the most significant cup for Physics
        physics_cup = physics_cups[exposed_physics_cups]
        total_significance += physics_cup[0]
        d -= physics_cup[1]
        exposed_physics_cups += 1

        # Expose the most significant cup for Informatics
        informatics_cup = informatics_cups[exposed_informatics_cups]
        total_significance += informatics_cup[0]
        d -= informatics_cup[1]
        exposed_informatics_cups += 1

    # Return the maximum total significance
    return total_significance

def main():
    n, m, d = map(int, input().split())
    physics_cups = []
    informatics_cups = []
    for i in range(n):
        c, w = map(int, input().split())
        physics_cups.append((c, w))
    for i in range(m):
        c, w = map(int, input().split())
        informatics_cups.append((c, w))
    print(get_max_total_significance(n, m, d, physics_cups, informatics_cups))

if __name__ == '__main__':
    main()

