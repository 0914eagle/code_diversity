
def calculate_instability(weights):
    # Calculate the instability of each tandem kayak
    tandem_instability = [abs(weights[i] - weights[i+1]) for i in range(0, len(weights), 2)]
    
    # Calculate the instability of each single kayak
    single_instability = [0] * (len(weights) // 2)
    
    # Calculate the total instability of all kayaks
    total_instability = sum(tandem_instability + single_instability)
    
    return total_instability

def solve(weights):
    # Find the minimum total instability by trying all possible combinations of tandem and single kayaks
    min_instability = float('inf')
    for i in range(len(weights) // 2):
        for j in range(len(weights) // 2):
            if i != j:
                tandem_instability = abs(weights[i] - weights[i+1]) + abs(weights[j] - weights[j+1])
                single_instability = abs(weights[i] - weights[j])
                total_instability = tandem_instability + single_instability
                if total_instability < min_instability:
                    min_instability = total_instability
    
    return min_instability

def main():
    n = int(input())
    weights = list(map(int, input().split()))
    print(solve(weights))

if __name__ == '__main__':
    main()

