
def solve(D, W, C):
    # Initialize variables
    total_smoothie = W
    containers = []
    current_container = 0
    current_distance = 0

    # While there is still smoothie left to bring
    while total_smoothie > 0:
        # Calculate the distance the monkey can walk with the current amount of smoothie
        distance_left = total_smoothie / C

        # If the distance left is less than the distance to the family, bring the remaining smoothie
        if distance_left < D:
            total_smoothie = 0
        # Otherwise, bring as much smoothie as possible and leave the rest in a container
        else:
            total_smoothie -= C * D
            containers.append(C * D)
            current_container += 1
            current_distance += D

    # Calculate the total amount of smoothie brought
    total_brought = sum(containers)

    return total_brought

