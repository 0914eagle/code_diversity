
def calculate_expected_weight(weights, likes):
    
    n = len(weights)
    likes_count = likes.count(True)
    likes_index = [i for i, x in enumerate(likes) if x]
    total_weight = sum(weights)
    expected_weight = [0] * n
    for i in range(n):
        if likes[i]:
            expected_weight[i] = (weights[i] + likes_count) / (total_weight + likes_count)
        else:
            expected_weight[i] = weights[i] / total_weight
    return expected_weight

def solve(n, m, weights, likes):
    
    expected_weight = calculate_expected_weight(weights, likes)
    result = []
    for i in range(n):
        gcd, x, y = extended_euclid(998244353, int(expected_weight[i] * 10**9 + 0.5))
        result.append((x * 998244353) % 998244353)
    return result

def extended_euclid(a, b):
    
    if a == 0:
        return b, 0, 1
    gcd, y, x = extended_euclid(b % a, a)
    return gcd, x - (b // a) * y, y

if __name__ == '__main__':
    n, m = map(int, input().split())
    weights = list(map(int, input().split()))
    likes = list(map(int, input().split()))
    result = solve(n, m, weights, likes)
    print(*result, sep='\n')

