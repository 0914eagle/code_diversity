
def get_max_bitwise_xor(l, r):
    max_value = 0
    for a in range(l, r + 1):
        for b in range(a, r + 1):
            max_value = max(max_value, a ^ b)
    return max_value

def main():
    l, r = map(int, input().split())
    print(get_max_bitwise_xor(l, r))

if __name__ == '__main__':
    main()

