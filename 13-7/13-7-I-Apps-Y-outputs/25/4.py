
import math

def calculate_probability(n):
    # Calculate the number of odd numbers up to n
    num_odd_numbers = math.floor(n / 2)
    # Calculate the total number of numbers up to n
    num_numbers = n
    # Calculate the probability that a is odd
    probability = num_odd_numbers / num_numbers
    return probability

def main():
    n = int(input())
    probability = calculate_probability(n)
    print(probability)

if __name__ == '__main__':
    main()

