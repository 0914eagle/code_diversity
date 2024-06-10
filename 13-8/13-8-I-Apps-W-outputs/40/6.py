
def get_expected_sum(N, K, p):
    # Calculate the expected sum for each combination of K dice
    expected_sums = []
    for i in range(N - K + 1):
        sum = 0
        for j in range(K):
            sum += p[i + j]
        expected_sums.append(sum)
    
    # Return the maximum expected sum
    return max(expected_sums)

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    print(get_expected_sum(N, K, p))

if __name__ == '__main__':
    main()

