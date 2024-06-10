
def get_total_instability(weights):
    # Calculate the total instability of the party
    total_instability = 0
    for i in range(len(weights) - 1):
        total_instability += abs(weights[i] - weights[i + 1])
    
    return total_instability

def solve(weights):
    # Find the minimum total instability by trying all possible combinations of tandem kayaks
    min_total_instability = float('inf')
    for i in range(len(weights) // 2):
        for j in range(i + 1, len(weights) // 2):
            total_instability = get_total_instability([weights[i], weights[j]] + weights[i + 1:j] + weights[j + 1:])
            if total_instability < min_total_instability:
                min_total_instability = total_instability
    
    return min_total_instability

if __name__ == '__main__':
    n = int(input())
    weights = [int(i) for i in input().split()]
    print(solve(weights))

