
def f1(n, a, b):
    # Calculate the sum of a[i] * b[i] for all i
    sum_ab = sum(a[i] * b[i] for i in range(n))
    # Calculate the sum of a[i] for all i
    sum_a = sum(a[i] for i in range(n))
    # Calculate the sum of b[i] for all i
    sum_b = sum(b[i] for i in range(n))
    # Calculate the sum of a[i] * b[i] for all i, but with the elements of b rearranged
    sum_ab_rearranged = 0
    for i in range(n):
        sum_ab_rearranged += a[i] * b[(i + 1) % n]
    # Return the minimum value of the two sums
    return min(sum_ab, sum_ab_rearranged)

def f2(n, a, b):
    # Calculate the sum of a[i] * b[i] for all i
    sum_ab = sum(a[i] * b[i] for i in range(n))
    # Calculate the sum of a[i] for all i
    sum_a = sum(a[i] for i in range(n))
    # Calculate the sum of b[i] for all i
    sum_b = sum(b[i] for i in range(n))
    # Calculate the sum of a[i] * b[i] for all i, but with the elements of b rearranged
    sum_ab_rearranged = 0
    for i in range(n):
        sum_ab_rearranged += a[i] * b[(i + n - 1) % n]
    # Return the minimum value of the two sums
    return min(sum_ab, sum_ab_rearranged)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(min(f1(n, a, b), f2(n, a, b)) % 998244353)

