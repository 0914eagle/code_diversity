
def construct_string(n, k, t):
    min_length = n + (k - 1)
    return t * (k // n) + t[:k % n]

if __name__ == "__main__":
    n, k = map(int, input().split())
    t = input().strip()
    print(construct_string(n, k, t))
