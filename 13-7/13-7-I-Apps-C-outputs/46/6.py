
def reconstruct_arrows(N, K, arrows):
    # Initialize a dictionary to map each person to their next position
    person_to_next_position = {}
    for i in range(N):
        person_to_next_position[i+1] = arrows[i]

    # Initialize a set to keep track of the visited persons
    visited_persons = set()

    # Initialize a list to store the final arrow placement
    arrow_placement = []

    # Loop through each person and their next position
    for i in range(N):
        # Get the current person and their next position
        current_person = i+1
        next_position = person_to_next_position[current_person]

        # If the next position is not in the visited persons set, add it to the set and the arrow placement list
        if next_position not in visited_persons:
            visited_persons.add(next_position)
            arrow_placement.append(next_position)
        # If the next position is in the visited persons set, it means we have found a loop, so we can break the loop
        else:
            break

    # If the number of visited persons is not equal to the number of persons, it means we have an impossible scenario
    if len(visited_persons) != N:
        return "Impossible"

    # If we have reached this point, it means we have found a valid arrow placement, so we return the arrow placement list
    return arrow_placement

