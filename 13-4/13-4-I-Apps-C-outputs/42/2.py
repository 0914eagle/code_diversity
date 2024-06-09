
def get_max_distinct_ranks(N, K, a, b):
    # Your code here
    return max_distinct_ranks

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    max_distinct_ranks = get_max_distinct_ranks(N, K, a, b)
    print(max_distinct_ranks)

if __name__ == '__main__':
    main()

