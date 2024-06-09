
def get_target_weight(weights):
    # Sort the weights in non-decreasing order
    weights.sort()
    
    # Initialize the target weight as the smallest weight
    target_weight = weights[0]
    
    # Iterate through the weights and find the smallest weight that divides the total weight into two equal parts
    for i in range(1, len(weights)):
        if weights[i] == target_weight:
            # If there are an even number of animals with weight equal to the target weight, divide them equally among the two groups
            if len(weights) % 2 == 0:
                return target_weight
            # If there are an odd number of animals with weight equal to the target weight, send one of them to work with the elves and divide the remaining evenly among the two groups
            else:
                return target_weight + 1
        elif weights[i] > target_weight:
            # If the current weight is greater than the target weight, move on to the next weight
            continue
        # If the current weight is less than the target weight, set the target weight to the current weight and continue iterating
        target_weight = weights[i]
    
    # If no target weight is found, return the smallest weight
    return target_weight

def main():
    # Read the number of animals and their weights from stdin
    num_animals = int(input())
    weights = []
    for _ in range(num_animals):
        weights.append(int(input()))
    
    # Call the get_target_weight function and print the result
    print(get_target_weight(weights))

if __name__ == '__main__':
    main()

