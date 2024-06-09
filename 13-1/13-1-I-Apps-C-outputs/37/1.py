
def f1(n, m, a, w):
    # Calculate the total weight of all pictures
    total_weight = sum(w)
    
    # Calculate the probability of each picture being displayed
    probabilities = [wi / total_weight for wi in w]
    
    # Calculate the expected weight of each picture after m visits
    expected_weights = [0] * n
    for i in range(n):
        if a[i] == 1:
            expected_weights[i] = w[i] + m
        else:
            expected_weights[i] = w[i] - m
    
    # Calculate the gcd of each expected weight
    gcds = [1] * n
    for i in range(n):
        gcds[i] = gcd(expected_weights[i], 998244353)
    
    # Calculate the final expected weights
    final_expected_weights = [0] * n
    for i in range(n):
        final_expected_weights[i] = expected_weights[i] // gcds[i]
    
    return final_expected_weights

def f2(...):
    ...

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    a = list(map(int, input().split()))
    w = list(map(int, input().split()))
    print(*f1(n, m, a, w), sep='\n')

