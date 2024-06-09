
import itertools

def get_sum_count(n, k):
    # Calculate the sum of the first n numbers
    sum_n = (n * (n + 1)) // 2
    
    # Get all possible combinations of k numbers from 1 to n
    combinations = itertools.combinations(range(1, n + 1), k)
    
    # Iterate over the combinations and calculate the sum
    count = 0
    for combination in combinations:
        count += sum_n - sum(combination)
    
    # Return the result modulo (10^9 + 7)
    return count % 1000000007

