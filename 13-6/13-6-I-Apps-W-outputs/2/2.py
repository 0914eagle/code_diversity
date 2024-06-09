
import itertools

def get_expected_length(n, roads):
    # Initialize the expected length as 0
    expected_length = 0
    
    # Iterate over all possible paths
    for path in itertools.permutations(range(1, n + 1)):
        # Calculate the length of the current path
        length = 0
        for i in range(n - 1):
            length += 1
            if path[i] != path[i + 1]:
                length += 1
        
        # Add the length of the current path to the expected length
        expected_length += length
    
    # Return the expected length divided by the number of possible paths
    return expected_length / math.factorial(n)

def main():
    n = int(input())
    roads = []
    for i in range(n - 1):
        u, v = map(int, input().split())
        roads.append((u, v))
    print(get_expected_length(n, roads))

if __name__ == '__main__':
    main()

