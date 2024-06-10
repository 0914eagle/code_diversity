
import sys

def get_tastiness(tastiness_matrix, n, cost_per_scoop, cost_per_cone):
    # Initialize the maximum tastiness and the corresponding number of scoops
    max_tastiness = 0
    num_scoops = 0
    
    # Iterate over all possible combinations of flavors
    for i in range(1, n+1):
        for flavor_combination in itertools.combinations(range(n), i):
            # Calculate the tastiness of the current combination of flavors
            current_tastiness = sum(tastiness_matrix[flavor][flavor_combination] for flavor in flavor_combination)
            
            # Calculate the cost of the current combination of flavors
            current_cost = i * cost_per_scoop + (i-1) * cost_per_cone
            
            # Update the maximum tastiness and the corresponding number of scoops if necessary
            if current_tastiness > max_tastiness:
                max_tastiness = current_tastiness
                num_scoops = i
    
    # Return the maximum tastiness and the corresponding number of scoops
    return max_tastiness, num_scoops

def main():
    # Read the input from stdin
    n, k, a, b = map(int, input().split())
    tastiness_matrix = []
    for _ in range(k):
        tastiness_matrix.append(list(map(int, input().split())))
    
    # Call the get_tastiness function to get the maximum tastiness and the corresponding number of scoops
    max_tastiness, num_scoops = get_tastiness(tastiness_matrix, n, a, b)
    
    # Print the maximum tastiness and the corresponding number of scoops
    print(max_tastiness, num_scoops)

if __name__ == '__main__':
    main()

