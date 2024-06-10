
def get_instability(weights):
    # Calculate the instability of each tandem kayak
    tandem_instability = [abs(weights[i] - weights[i+1]) for i in range(0, len(weights), 2)]
    
    # Calculate the instability of each single kayak
    single_instability = [weights[i] for i in range(1, len(weights), 2)]
    
    # Calculate the total instability
    total_instability = sum(tandem_instability) + sum(single_instability)
    
    return total_instability

def main():
    n = int(input())
    weights = list(map(int, input().split()))
    print(get_instability(weights))

if __name__ == '__main__':
    main()

