
import math

def get_probability(n):
    # Calculate the number of possible combinations
    num_combinations = math.factorial(n)
    
    # Calculate the number of combinations where no one gives a gift to themselves
    num_valid_combinations = 0
    for i in range(1, n+1):
        num_valid_combinations += math.factorial(n-1) / math.factorial(i) / math.factorial(n-i)
    
    # Calculate the probability
    probability = 1 - num_valid_combinations / num_combinations
    
    return probability

def main():
    n = int(input())
    print(get_probability(n))

if __name__ == '__main__':
    main()

