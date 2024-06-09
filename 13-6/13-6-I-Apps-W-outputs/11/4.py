
def get_target_weight(weights):
    # Sort the weights in non-decreasing order
    weights.sort()
    
    # Initialize the target weight as the smallest weight
    target_weight = weights[0]
    
    # Iterate through the weights and find the first weight that is greater than the target weight
    for i in range(1, len(weights)):
        if weights[i] > target_weight:
            break
        target_weight += 1
    
    return target_weight

def get_group_weights(weights, target_weight):
    # Initialize the group weights as empty lists
    group1 = []
    group2 = []
    
    # Iterate through the weights and add them to the appropriate group
    for weight in weights:
        if weight <= target_weight:
            group1.append(weight)
        else:
            group2.append(weight)
    
    return group1, group2

def solve(weights):
    # Get the target weight
    target_weight = get_target_weight(weights)
    
    # Get the group weights
    group1, group2 = get_group_weights(weights, target_weight)
    
    # Return the smallest integer target weight
    return target_weight

if __name__ == '__main__':
    weights = [3, 6, 1, 2]
    print(solve(weights))

