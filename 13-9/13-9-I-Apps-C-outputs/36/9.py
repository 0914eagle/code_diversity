
def get_remainder(x, k, ancient_values):
    # Check if k is one of the ancient values
    if k in ancient_values:
        return x % k
    
    # Check if any of the ancient values is a factor of k
    for ancient_value in ancient_values:
        if k % ancient_value == 0:
            return x % ancient_value
    
    # If none of the above conditions are met, Arya cannot determine the remainder
    return -1

def has_winning_strategy(n, k, ancient_values):
    # Check if Arya can determine the remainder for any value of x
    for x in range(1, 1000001):
        if get_remainder(x, k, ancient_values) != -1:
            return "Yes"
    
    # If Arya cannot determine the remainder for any value of x, they don't have a winning strategy
    return "No"

if __name__ == '__main__':
    n, k = map(int, input().split())
    ancient_values = list(map(int, input().split()))
    print(has_winning_strategy(n, k, ancient_values))

