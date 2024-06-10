
def construct_min_string(n, k, t):
    min_length = n + (k - 1)
    return t * (min_length // n) + t[:min_length % n]

if __name__ == "__main__":
    n, k = map(int, input().split())
    t = input().strip()
    print(construct_min_string(n, k, t))
