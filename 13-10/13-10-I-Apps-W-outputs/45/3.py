
def get_instability(weights):
    # Calculate the instability of each tandem kayak
    tandem_instability = [abs(weights[i] - weights[i+1]) for i in range(0, len(weights), 2)]
    
    # Calculate the instability of each single kayak
    single_instability = [0] * (len(weights) // 2)
    
    # Calculate the total instability
    total_instability = sum(tandem_instability) + sum(single_instability)
    
    return total_instability

def solve(n, weights):
    # Sort the weights in ascending order
    weights.sort()
    
    # Initialize the minimum total instability
    min_total_instability = float('inf')
    
    # Iterate over all possible combinations of tandem kayaks
    for i in range(1, len(weights) // 2):
        # Calculate the total instability for this combination
        total_instability = get_instability(weights[:i*2]) + get_instability(weights[i*2:])
        
        # Update the minimum total instability
        if total_instability < min_total_instability:
            min_total_instability = total_instability
    
    return min_total_instability

if __name__ == '__main__':
    n = int(input())
    weights = list(map(int, input().split()))
    print(solve(n, weights))

