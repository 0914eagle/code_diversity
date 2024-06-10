
def get_instability(weights):
    # Calculate the instability of each tandem kayak
    tandem_instability = [abs(weights[i] - weights[i+1]) for i in range(0, len(weights), 2)]
    
    # Calculate the instability of each single kayak
    single_instability = [0] * len(weights)
    for i in range(len(weights)):
        if i % 2 == 0:
            single_instability[i] = tandem_instability[i // 2]
        else:
            single_instability[i] = 0
    
    # Calculate the total instability of the journey
    total_instability = sum(single_instability)
    
    return total_instability

def get_optimal_seating(weights):
    # Calculate the instability of each tandem kayak
    tandem_instability = [abs(weights[i] - weights[i+1]) for i in range(0, len(weights), 2)]
    
    # Calculate the instability of each single kayak
    single_instability = [0] * len(weights)
    for i in range(len(weights)):
        if i % 2 == 0:
            single_instability[i] = tandem_instability[i // 2]
        else:
            single_instability[i] = 0
    
    # Calculate the total instability of the journey
    total_instability = sum(single_instability)
    
    # Initialize the optimal seating arrangement
    optimal_seating = [-1] * len(weights)
    
    # Loop through each person and assign them to a kayak with the least instability
    for i in range(len(weights)):
        least_instability = float('inf')
        least_instability_index = -1
        for j in range(len(single_instability)):
            if single_instability[j] < least_instability:
                least_instability = single_instability[j]
                least_instability_index = j
        optimal_seating[i] = least_instability_index
        single_instability[least_instability_index] = float('inf')
    
    return optimal_seating

def main():
    n = int(input())
    weights = list(map(int, input().split()))
    optimal_seating = get_optimal_seating(weights)
    total_instability = get_instability(weights)
    print(total_instability)

if __name__ == '__main__':
    main()

