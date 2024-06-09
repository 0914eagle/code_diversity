
import math

def get_probability(m, n, t, p):
    # Calculate the probability that a single person wins the lottery
    probability = n / m
    
    # Calculate the probability that p people win the lottery
    probability = probability ** p
    
    # Calculate the probability that a person wins at most t tickets
    probability = probability * (1 - ((t - 1) / m)) ** p
    
    return probability

def main():
    m, n, t, p = map(int, input().split())
    print(get_probability(m, n, t, p))

if __name__ == "__main__":
    main()

