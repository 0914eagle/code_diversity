
def solve(n, observations):
    # Initialize a dictionary to store the costume assignments
    costumes = {}

    # Iterate over the observations
    for i, (l, r, x) in enumerate(observations):
        # Get the indices of the children to the left and right of child i
        left = (i - l) % n
        right = (i + r) % n

        # If x is 0, then an even number of children between left and right are wearing the orange pumpkin costume
        if x == 0:
            # Iterate over the children between left and right
            for j in range(left, right + 1):
                # If the child is not already assigned a costume, assign it the orange pumpkin costume
                if j not in costumes:
                    costumes[j] = "orange pumpkin"
                # If the child is already assigned a costume and it's not orange pumpkin, then it's a contradiction
                elif costumes[j] != "orange pumpkin":
                    return 0
        # If x is 1, then an odd number of children between left and right are wearing the orange pumpkin costume
        elif x == 1:
            # Iterate over the children between left and right
            for j in range(left, right + 1):
                # If the child is not already assigned a costume, assign it the black bat costume
                if j not in costumes:
                    costumes[j] = "black bat"
                # If the child is already assigned a costume and it's not black bat, then it's a contradiction
                elif costumes[j] != "black bat":
                    return 0

    # If we reach this point, then we have successfully assigned costumes to all children
    return len(costumes) % (10**9 + 7)

