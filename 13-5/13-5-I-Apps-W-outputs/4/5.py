
def solve(n, k, stages):
    # Initialize a list to store the weights of the stages
    weights = [0] * 26
    for i in range(n):
        # Convert the character to its index in the alphabet
        index = ord(stages[i]) - ord('a')
        # Calculate the weight of the stage
        weights[index] += i + 1
    
    # Initialize a list to store the selected stages
    selected = [False] * 26
    # Initialize the total weight of the rocket to 0
    total_weight = 0
    
    for i in range(k):
        # Find the stage with the minimum weight that has not been selected yet
        min_index = 0
        for j in range(26):
            if not selected[j] and weights[j] < weights[min_index]:
                min_index = j
        # If there is no stage that has not been selected yet, return -1
        if min_index == 0:
            return -1
        # Select the stage with the minimum weight
        selected[min_index] = True
        # Add the weight of the selected stage to the total weight of the rocket
        total_weight += weights[min_index]
    
    # Return the total weight of the rocket
    return total_weight

