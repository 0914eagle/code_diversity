
def get_input():
    return list(map(int, input().split()))

def get_max_product(a, b, c, d):
    return max(a*c, a*d, b*c, b*d)

def main():
    a, b, c, d = get_input()
    print(get_max_product(a, b, c, d))

if __name__ == '__main__':
    main()

