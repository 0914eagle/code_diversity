
def get_max_xor(l, r):
    max_xor = 0
    for a in range(l, r + 1):
        for b in range(a, r + 1):
            xor = a ^ b
            if xor > max_xor:
                max_xor = xor
    return max_xor

def main():
    l, r = map(int, input().split())
    print(get_max_xor(l, r))

if __name__ == '__main__':
    main()

