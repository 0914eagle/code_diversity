
def get_max_xor(l, r):
    max_xor = 0
    for a in range(l, r + 1):
        for b in range(a, r + 1):
            max_xor = max(max_xor, a ^ b)
    return max_xor

def main():
    l, r = map(int, input().split())
    print(get_max_xor(l, r))

if __name__ == '__main__':
    main()

