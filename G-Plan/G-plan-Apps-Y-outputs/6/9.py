
def count_good_candies(n, weights):
    odd_prefix_sum = [0] * (n + 1)
    even_prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        odd_prefix_sum[i] = odd_prefix_sum[i - 1] + (weights[i - 1] if i % 2 == 1 else 0)
        even_prefix_sum[i] = even_prefix_sum[i - 1] + (weights[i - 1] if i % 2 == 0 else 0)

    good_candies = 0
    for i in range(1, n + 1):
        odd_sum = odd_prefix_sum[i - 1] + even_prefix_sum[n] - even_prefix_sum[i]
        even_sum = even_prefix_sum[i - 1] + odd_prefix_sum[n] - odd_prefix_sum[i]
        if odd_sum == even_sum:
            good_candies += 1

    return good_candies

if __name__ == "__main__":
    n = int(input())
    weights = list(map(int, input().split()))
    result = count_good_candies(n, weights)
    print(result)
