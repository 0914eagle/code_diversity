
def get_min_turns(n, A, B, intersections):
    # Initialize variables
    min_turns = float('inf')
    correct_person = None

    # Iterate over all possible intersections
    for i in range(n):
        # If the intersection is visible from both A and B, continue
        if intersections[i][2] == 0:
            continue

        # If the intersection is visible from A but not B, or vice versa, the correct person is the one who is currently at the intersection
        if (intersections[i][2] == 1 and i == A) or (intersections[i][2] == 0 and i == B):
            correct_person = i
            break

    # If no intersection is visible from both A and B, return "indistinguishable"
    if correct_person is None:
        return "indistinguishable"

    # Calculate the minimum number of turns it takes to get to the correct intersection
    min_turns = abs(correct_person - A) + abs(correct_person - B)

    return min_turns

def main():
    n, A, B = map(int, input().split())
    intersections = []
    for i in range(n):
        l, r, t = map(int, input().split())
        intersections.append([l, r, t])
    print(get_min_turns(n, A, B, intersections))

if __name__ == '__main__':
    main()

