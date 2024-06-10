
import itertools
import math

def explosion_probability(n, m, d):
    # Calculate the probability of killing each minion
    probabilities = [minion_probability(n, m, d) for _ in range(m)]
    
    # Calculate the probability of killing all minions
    return sum(probabilities)

def minion_probability(n, m, d):
    # Calculate the number of ways to kill a minion
    num_ways = math.comb(m, d)
    
    # Calculate the number of ways to kill all minions
    denom = math.comb(m, n)
    
    # Calculate the probability of killing all minions
    return num_ways / denom

def input_parser(input_string):
    n, m, d = input_string.split()
    return int(n), int(m), int(d)

def main():
    input_string = input()
    n, m, d = input_parser(input_string)
    print(explosion_probability(n, m, d))

if __name__ == '__main__':
    main()

