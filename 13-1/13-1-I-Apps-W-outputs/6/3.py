
def get_max_total_significance(n, m, d, physics_cups, informatics_cups):
    # Sort the cups by their significance in descending order
    physics_cups.sort(key=lambda x: x[0], reverse=True)
    informatics_cups.sort(key=lambda x: x[0], reverse=True)

    # Initialize the maximum total significance and the current total width
    max_total_significance = 0
    current_total_width = 0

    # Loop through the cups and add them to the shelf if they fit
    for physics_cup, informatics_cup in zip(physics_cups, informatics_cups):
        # Check if the cup fits on the shelf
        if current_total_width + physics_cup[1] + informatics_cup[1] <= d:
            # Add the cup to the shelf
            current_total_width += physics_cup[1] + informatics_cup[1]

            # Update the maximum total significance
            max_total_significance += physics_cup[0] + informatics_cup[0]

    # Return the maximum total significance
    return max_total_significance

def main():
    n, m, d = map(int, input().split())
    physics_cups = []
    informatics_cups = []
    for i in range(n):
        physics_cups.append(list(map(int, input().split())))
    for i in range(m):
        informatics_cups.append(list(map(int, input().split())))
    print(get_max_total_significance(n, m, d, physics_cups, informatics_cups))

if __name__ == '__main__':
    main()

