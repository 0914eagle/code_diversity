
def find_good_candies(n, weights):
    prefix_sum_odd = [0] * (n + 1)
    prefix_sum_even = [0] * (n + 1)
    for i in range(n):
        prefix_sum_odd[i + 1] = prefix_sum_odd[i] + (weights[i] if i % 2 == 0 else 0)
        prefix_sum_even[i + 1] = prefix_sum_even[i] + (weights[i] if i % 2 == 1 else 0)

    good_candies = 0
    for i in range(n):
        odd_sum = prefix_sum_odd[i] + prefix_sum_even[n] - prefix_sum_even[i + 1]
        even_sum = prefix_sum_even[i] + prefix_sum_odd[n] - prefix_sum_odd[i + 1]
        if odd_sum == even_sum:
            good_candies += 1

    return good_candies

if __name__ == "__main__":
    n = int(input())
    weights = list(map(int, input().split()))
    result = find_good_candies(n, weights)
    print(result)
