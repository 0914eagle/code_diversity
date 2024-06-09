
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
    m = int(input())
    weights = []
    for i in range(m):
        weights.append(int(input()))
    print(get_target_weight(weights))

if __name__ == '__main__':
    main()

