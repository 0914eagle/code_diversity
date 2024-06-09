
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

