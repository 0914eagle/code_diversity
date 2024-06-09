
def get_target_weight(weights):
    # Sort the weights in non-decreasing order
    weights.sort()
    
    # Initialize the target weight as the median of the weights
    target_weight = weights[len(weights) // 2]
    
    # Loop through the weights and check if they are equal to the target weight
    for weight in weights:
        if weight == target_weight:
            # If there are an even number of weights equal to the target weight, divide them evenly among the two groups
            if len(weights) % 2 == 0:
                return target_weight
            # If there is an odd number of weights equal to the target weight, send one of them to work with the elves and divide the remaining evenly among the two groups
            else:
                return target_weight + 1
    
    # If no weights are equal to the target weight, return the target weight
    return target_weight

def main():
    weights = [int(input()) for _ in range(int(input()))]
    print(get_target_weight(weights))

if __name__ == '__main__':
    main()

