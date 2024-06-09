
def get_max_total_significance(n, m, d, physics_cups, informatics_cups):
    # Sort the cups by their significance in descending order
    physics_cups.sort(key=lambda x: x[0], reverse=True)
    informatics_cups.sort(key=lambda x: x[0], reverse=True)

    # Initialize the variables to keep track of the exposed cups
    exposed_physics_cups = []
    exposed_informatics_cups = []
    total_significance = 0

    # Loop through the cups and expose them on the shelf
    while physics_cups or informatics_cups:
        # If there is no more space on the shelf, break the loop
        if d < sum(map(lambda x: x[1], exposed_physics_cups + exposed_informatics_cups)):
            break

        # If there are no more Physics cups, expose Informatics cups
        if not physics_cups:
            cup = informatics_cups.pop()
            exposed_informatics_cups.append(cup)
            total_significance += cup[0]
            continue

        # If there are no more Informatics cups, expose Physics cups
        if not informatics_cups:
            cup = physics_cups.pop()
            exposed_physics_cups.append(cup)
            total_significance += cup[0]
            continue

        # Compare the significance of the top Physics and Informatics cups
        physics_cup = physics_cups[-1]
        informatics_cup = informatics_cups[-1]
        if physics_cup[0] >= informatics_cup[0]:
            cup = physics_cups.pop()
            exposed_physics_cups.append(cup)
            total_significance += cup[0]
        else:
            cup = informatics_cups.pop()
            exposed_informatics_cups.append(cup)
            total_significance += cup[0]

    # Return the maximum total significance
    return total_significance

def main():
    n, m, d = map(int, input().split())
    physics_cups = []
    informatics_cups = []
    for _ in range(n):
        c, w = map(int, input().split())
        physics_cups.append((c, w))
    for _ in range(m):
        c, w = map(int, input().split())
        informatics_cups.append((c, w))
    print(get_max_total_significance(n, m, d, physics_cups, informatics_cups))

if __name__ == '__main__':
    main()

