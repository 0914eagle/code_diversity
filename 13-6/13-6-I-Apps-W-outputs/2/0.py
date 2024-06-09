
import math

def get_expected_length(n, roads):
    # Initialize the probability of reaching each city
    probabilities = [1] * n
    # Initialize the total expected length
    total_expected_length = 0
    
    for i in range(n):
        # Get the cities connected to the current city
        connected_cities = [road[1] for road in roads if road[0] == i + 1]
        # Get the number of connected cities
        num_connected_cities = len(connected_cities)
        # If there are no connected cities, break the loop
        if num_connected_cities == 0:
            break
        # Calculate the probability of reaching each connected city
        probabilities[i] = 1 / num_connected_cities
        # Calculate the expected length of reaching each connected city
        expected_lengths = [probabilities[i] * (i + 1) for i in connected_cities]
        # Add the expected lengths to the total expected length
        total_expected_length += sum(expected_lengths)
    
    return total_expected_length

def main():
    n = int(input())
    roads = []
    for i in range(n - 1):
        u, v = map(int, input().split())
        roads.append([u, v])
    print(get_expected_length(n, roads))

if __name__ == '__main__':
    main()

