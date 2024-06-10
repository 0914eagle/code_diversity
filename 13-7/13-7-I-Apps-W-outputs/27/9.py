
import itertools

def get_factors(n):
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if n // i != i:
                factors.append(n // i)
    return sorted(factors)

def count_ways(n, k, S):
    # Initialize a dictionary to store the number of ways for each sum
    dp = {0: 1}
    
    # Iterate over the numbers
    for i in range(1, n+1):
        # Get the factors of the current number
        factors = get_factors(i)
        
        # Iterate over the possible sums
        for j in range(S+1):
            # If the current sum is already in the dictionary, update the number of ways
            if j in dp:
                dp[j] += len(factors)
            # If the current sum is not in the dictionary, add it and set the number of ways to the number of factors
            else:
                dp[j] = len(factors)
    
    # Return the number of ways for the given sum
    return dp[S]

def main():
    n, k, S = map(int, input().split())
    print(count_ways(n, k, S))

if __name__ == '__main__':
    main()

