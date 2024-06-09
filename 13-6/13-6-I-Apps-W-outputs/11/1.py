
def get_target_weight(weights):
    # Sort the weights in non-decreasing order
    weights.sort()
    
    # Initialize the target weight as the median of the weights
    target_weight = weights[len(weights) // 2]
    
    # Loop through the weights and check if the sum of the weights
    # in one group is equal to the sum of the weights in the other group
    for i in range(len(weights)):
        if sum(weights[:i]) == sum(weights[i:]):
            return target_weight
    
    # If no such target weight is found, return the maximum weight
    return max(weights)

def main():
    m = int(input())
    weights = []
    for i in range(m):
        weights.append(int(input()))
    print(get_target_weight(weights))

if __name__ == '__main__':
    main()

