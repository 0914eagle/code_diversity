
import math

def is_connected(n):
    # Calculate the number of possible connections between cities
    num_possible_connections = n * (n - 1) / 2
    
    # Calculate the number of possible connected networks
    num_possible_connected_networks = math.comb(n, 2)
    
    # Calculate the probability of a connected network
    probability = num_possible_connected_networks / num_possible_connections
    
    return probability

