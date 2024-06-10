
def construct_string(n, k, t):
    min_length = n + (k - 1)
    return t * ((min_length // n) + 1)

if __name__ == "__main__":
    n, k = map(int, input().split())
    t = input().strip()
    result = construct_string(n, k, t)
    print(result)
