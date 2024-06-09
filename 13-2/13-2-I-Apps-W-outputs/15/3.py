
def get_maximum_sum(n, m, k, p):
    # Sort the array in non-decreasing order
    p.sort()
    # Initialize the maximum sum and the current sum
    max_sum = 0
    current_sum = 0
    # Loop through the array and choose the k pairs with the maximum sum
    for i in range(n - k * m + 1):
        current_sum += p[i]
        if i >= k * m - 1:
            max_sum = max(max_sum, current_sum)
            current_sum -= p[i - k * m + 1]
    return max_sum

def main():
    n, m, k = map(int, input().split())
    p = list(map(int, input().split()))
    print(get_maximum_sum(n, m, k, p))

if __name__ == '__main__':
    main()

