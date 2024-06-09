
import math

def is_connected(n):
    # Calculate the number of possible connections
    num_possible_connections = n * (n - 1) / 2
    
    # Calculate the number of possible connected networks
    num_connected_networks = 0
    for i in range(1, n + 1):
        num_connected_networks += math.comb(n, i)
    
    # Calculate the probability of a connected network
    probability = num_connected_networks / num_possible_connections
    
    return probability

