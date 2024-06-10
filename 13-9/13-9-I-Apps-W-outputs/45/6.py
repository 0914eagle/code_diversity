
import math

def get_expected_value(n, k):
    # Initialize the expected value to 1
    expected_value = 1
    
    # Loop through each step
    for i in range(k):
        # Get the divisors of the current value
        divisors = get_divisors(n)
        
        # Calculate the probability of each divisor
        probabilities = [1 / len(divisors)] * len(divisors)
        
        # Calculate the expected value of the next step
        expected_value = sum(d * p for d, p in zip(divisors, probabilities))
        
    return expected_value

def get_divisors(n):
    # Get the list of divisors
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
    
    # Sort the divisors in ascending order
    divisors.sort()
    
    return divisors

def main():
    n, k = map(int, input().split())
    print(get_expected_value(n, k))

if __name__ == '__main__':
    main()

