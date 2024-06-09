
def get_maximum_bitwise_xor(l, r):
    maximum = 0
    for a in range(l, r + 1):
        for b in range(a, r + 1):
            maximum = max(maximum, a ^ b)
    return maximum

def main():
    l, r = map(int, input().split())
    print(get_maximum_bitwise_xor(l, r))

if __name__ == '__main__':
    main()

