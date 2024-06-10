
def input_data():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    return N, K, p

def expected_sum(p, K):
    # Calculate the expected sum for each possible combination of K dice
    expected_sums = []
    for i in range(N - K + 1):
        sum = 0
        for j in range(K):
            sum += p[i + j]
        expected_sums.append(sum)
    
    # Return the maximum expected sum
    return max(expected_sums)

def main():
    N, K, p = input_data()
    print(expected_sum(p, K))

if __name__ == '__main__':
    main()

