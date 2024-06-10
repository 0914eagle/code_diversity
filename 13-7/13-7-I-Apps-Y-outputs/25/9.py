
def get_probability(n):
    # Calculate the number of odd numbers less than or equal to n
    num_of_odds = (n // 2) + (n % 2)
    
    # Calculate the total number of positive integers less than or equal to n
    num_of_integers = n
    
    # Calculate the probability that a is odd
    probability = num_of_odds / num_of_integers
    
    # Return the probability
    return probability

def main():
    # Accept a single integer input from stdin
    n = int(input())
    
    # Calculate the probability that a is odd
    probability = get_probability(n)
    
    # Print the probability
    print(probability)

if __name__ == '__main__':
    main()

