
def calculate_sum(a, c):
    a.sort()
    n = len(a)
    skip = n // c
    return sum(a[skip:])

if __name__ == "__main__":
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    result = calculate_sum(a, c)
    print(result)
