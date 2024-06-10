
def get_max_coins(a, b):
    return max(a + (a - 1), a + b)

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(get_max_coins(a, b))
