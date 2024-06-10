
def get_xor_sequence(a, n):
    xor_seq = [0] * (n + 1)
    xor_seq[0] = a[0]
    for i in range(1, n):
        xor_seq[i] = xor_seq[i - 1] ^ a[i]
    return xor_seq

def count_pairs(a, n):
    xor_seq = get_xor_sequence(a, n)
    count = 0
    for i in range(n):
        for j in range(i, n):
            if xor_seq[i] == xor_seq[j] and xor_seq[i] == xor_seq[0]:
                count += 1
    return count

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(count_pairs(a, n))

if __name__ == '__main__':
    main()

