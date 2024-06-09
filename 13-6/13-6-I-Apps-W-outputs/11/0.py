
def get_target_weight(weights):
    # Sort the weights in non-decreasing order
    weights.sort()
    # Initialize the target weight as the smallest weight
    target_weight = weights[0]
    # Initialize the sum of weights as the sum of all weights
    total_weight = sum(weights)
    # Iterate through the weights and find the first weight that is greater than the target weight
    for weight in weights:
        if weight > target_weight:
            # If the weight is greater than the target weight, break the loop
            break
        # Otherwise, increase the target weight by the current weight
        target_weight += weight
    # Return the target weight
    return target_weight

def get_grouped_weights(weights, target_weight):
    # Initialize two lists to store the weights of the two groups
    group1 = []
    group2 = []
    # Iterate through the weights and append them to the appropriate group
    for weight in weights:
        if weight <= target_weight:
            group1.append(weight)
        else:
            group2.append(weight)
    # Return the two lists of grouped weights
    return group1, group2

def get_even_distribution(weights):
    # Sort the weights in non-decreasing order
    weights.sort()
    # Initialize the target weight as the smallest weight
    target_weight = weights[0]
    # Initialize the sum of weights as the sum of all weights
    total_weight = sum(weights)
    # Iterate through the weights and find the first weight that is greater than the target weight
    for weight in weights:
        if weight > target_weight:
            # If the weight is greater than the target weight, break the loop
            break
        # Otherwise, increase the target weight by the current weight
        target_weight += weight
    # Return the target weight
    return target_weight

def get_odd_distribution(weights):
    # Sort the weights in non-decreasing order
    weights.sort()
    # Initialize the target weight as the smallest weight
    target_weight = weights[0]
    # Initialize the sum of weights as the sum of all weights
    total_weight = sum(weights)
    # Iterate through the weights and find the first weight that is greater than the target weight
    for weight in weights:
        if weight > target_weight:
            # If the weight is greater than the target weight, break the loop
            break
        # Otherwise, increase the target weight by the current weight
        target_weight += weight
    # Return the target weight
    return target_weight

def main():
    # Read the number of animals from stdin
    num_animals = int(input())
    # Read the weights of the animals from stdin
    weights = list(map(int, input().split()))
    # Get the target weight
    target_weight = get_target_weight(weights)
    # Get the grouped weights
    group1, group2 = get_grouped_weights(weights, target_weight)
    # Print the grouped weights
    print(group1)
    print(group2)

if __name__ == '__main__':
    main()

