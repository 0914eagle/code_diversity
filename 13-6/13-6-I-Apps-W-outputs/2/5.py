
import itertools

def get_expected_length(n, roads):
    # Initialize a dictionary to store the expected length for each city
    expected_length = {1: 0}
    
    # Iterate through each road
    for u, v in roads:
        # If the city has not been visited yet, set the expected length to 0
        if u not in expected_length:
            expected_length[u] = 0
        if v not in expected_length:
            expected_length[v] = 0
        
        # Update the expected length for the city
        expected_length[u] += 1 / n
        expected_length[v] += 1 / n
    
    return expected_length[n]

def main():
    n = int(input())
    roads = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        roads.append((u, v))
    print(get_expected_length(n, roads))

if __name__ == '__main__':
    main()

