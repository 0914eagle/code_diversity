
def input_data():
    n = int(input())
    weights = list(map(int, input().split()))
    return n, weights

def min_total_instability(n, weights):
    # Initialize the total instability to infinity
    total_instability = float('inf')
    
    # Loop through all possible combinations of tandem kayaks
    for i in range(0, len(weights), 2):
        # Calculate the instability of the current combination
        instability = abs(weights[i] - weights[i+1])
        
        # If the instability is less than the current minimum, update the minimum
        if instability < total_instability:
            total_instability = instability
    
    return total_instability

def main():
    n, weights = input_data()
    print(min_total_instability(n, weights))

if __name__ == '__main__':
    main()

