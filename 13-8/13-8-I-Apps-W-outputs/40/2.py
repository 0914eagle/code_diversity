
def input_data():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    return N, K, p

def get_expected_value(p, K):
    expected_value = 0
    for i in range(K):
        expected_value += p[i]
    return expected_value

def get_maximum_expected_value(p, K, N):
    maximum_expected_value = 0
    for i in range(N - K + 1):
        expected_value = get_expected_value(p[i:i+K], K)
        if expected_value > maximum_expected_value:
            maximum_expected_value = expected_value
    return maximum_expected_value

def main():
    N, K, p = input_data()
    print(get_maximum_expected_value(p, K, N))

if __name__ == '__main__':
    main()

