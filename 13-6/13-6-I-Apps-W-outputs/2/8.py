
def get_expected_length(n, roads):
    # Initialize a dictionary to store the probability of reaching each city
    probabilities = {}
    
    # Initialize the probability of reaching the first city to 1
    probabilities[1] = 1
    
    # Loop through each road
    for u, v in roads:
        # If the probability of reaching the first city is not 0
        if probabilities[u] != 0:
            # Add the probability of reaching the second city to the dictionary
            probabilities[v] = probabilities[v] + probabilities[u]
    
    # Calculate the expected length of the journey
    expected_length = sum(probabilities[i] * i for i in range(1, n + 1))
    
    return expected_length

def main():
    n = int(input())
    roads = []
    
    for _ in range(n - 1):
        u, v = map(int, input().split())
        roads.append((u, v))
    
    expected_length = get_expected_length(n, roads)
    print(expected_length)

if __name__ == '__main__':
    main()

