
def get_max_birds(l, d, n):
    return int((l - n * d - 12) / (d + 2))

def main():
    l, d, n = map(int, input().split())
    print(get_max_birds(l, d, n))

if __name__ == '__main__':
    main()

