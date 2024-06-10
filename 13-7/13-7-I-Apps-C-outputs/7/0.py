
def get_min_turns(A, B, intersections):
    # Initialize variables
    min_turns = 0
    current_intersection = A

    # Loop through the intersections
    for i in range(len(intersections)):
        # If the current intersection is the same as A or B, skip it
        if current_intersection in [A, B]:
            continue

        # Get the left and right turns for the current intersection
        left_turn = intersections[current_intersection][0]
        right_turn = intersections[current_intersection][1]

        # If the current intersection is visible from both A and B, return indistinguishable
        if intersections[current_intersection][2] == 1 and current_intersection in [A, B]:
            return "indistinguishable"

        # If the current intersection is visible from A but not B, return the number of turns it takes to get to the current intersection from A
        if intersections[current_intersection][2] == 1 and current_intersection == A:
            return min_turns

        # If the current intersection is visible from B but not A, return the number of turns it takes to get to the current intersection from B
        if intersections[current_intersection][2] == 1 and current_intersection == B:
            return min_turns

        # Update the current intersection and the number of turns
        current_intersection = left_turn if current_intersection == A else right_turn
        min_turns += 1

    # If the tower is not visible from either A or B, return indistinguishable
    return "indistinguishable"

def main():
    # Read the input
    n, A, B = map(int, input().split())
    intersections = [tuple(map(int, input().split())) for _ in range(n)]

    # Call the get_min_turns function and print the result
    print(get_min_turns(A, B, intersections))

if __name__ == '__main__':
    main()

