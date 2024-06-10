
import math

def get_expected_value(n, k):
    # Calculate the divisors of n
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
    
    # Calculate the expected value after k steps
    expected_value = 0
    for divisor in divisors:
        expected_value += divisor * pow(divisor, k, 1000000007)
    expected_value %= 1000000007
    
    return expected_value

def main():
    n, k = map(int, input().split())
    print(get_expected_value(n, k))

if __name__ == '__main__':
    main()

