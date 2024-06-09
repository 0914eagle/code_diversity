
def get_bitwise_xor_pairs(l, r):
    pairs = []
    for a in range(l, r+1):
        for b in range(a, r+1):
            pairs.append(a ^ b)
    return pairs

def get_max_bitwise_xor(l, r):
    pairs = get_bitwise_xor_pairs(l, r)
    return max(pairs)

if __name__ == '__main__':
    l, r = map(int, input().split())
    print(get_max_bitwise_xor(l, r))

