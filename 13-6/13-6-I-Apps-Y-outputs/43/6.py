
def get_number_of_ways(N, K):
    if N == 1:
        return K
    if N == 2:
        return K * (K - 1)
    return get_number_of_ways(N - 1, K) * (K - 1) + get_number_of_ways(N - 2, K)

def main():
    N, K = map(int, input().split())
    print(get_number_of_ways(N, K))

if __name__ == '__main__':
    main()

