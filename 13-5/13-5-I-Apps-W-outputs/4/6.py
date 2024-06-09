
def get_min_weight(n, k, stages):
    # Initialize a dictionary to store the weight of each stage
    weights = {}
    for i in range(n):
        weights[stages[i]] = i + 1
    
    # Initialize a list to store the stages in the correct order
    ordered_stages = []
    
    # Loop through the stages and add them to the list in the correct order
    for i in range(n):
        stage = stages[i]
        if len(ordered_stages) == 0:
            ordered_stages.append(stage)
        else:
            # Check if the stage can be added to the list
            can_add = True
            for j in range(len(ordered_stages)):
                if ord(stage) - ord(ordered_stages[j]) <= 2:
                    can_add = False
                    break
            if can_add:
                ordered_stages.append(stage)
    
    # If the list of stages is not equal to k, it is impossible to build the rocket
    if len(ordered_stages) != k:
        return -1
    
    # Calculate the total weight of the rocket
    total_weight = 0
    for stage in ordered_stages:
        total_weight += weights[stage]
    
    return total_weight

